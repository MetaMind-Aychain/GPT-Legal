import os
import sys

import fire
import gradio as gr
import torch
import transformers
from peft import PeftModel
from transformers import GenerationConfig, LlamaForCausalLM, LlamaTokenizer, AutoModel, AutoTokenizer, AutoModelForCausalLM

from utils.callbacks import Iteratorize, Stream
from utils.prompter import Prompter

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

try:
    if torch.backends.mps.is_available():
        device = "mps"
except: 
    pass


# US Legal Provisions and Cases Database
US_LEGAL_PROVISIONS = {
    "Constitutional Law": [
        {
            "title": "First Amendment",
            "provision": "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.",
            "article": "Amendment I"
        },
        {
            "title": "Fourth Amendment",
            "provision": "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.",
            "article": "Amendment IV"
        },
        {
            "title": "Fifth Amendment",
            "provision": "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation.",
            "article": "Amendment V"
        },
        {
            "title": "Fourteenth Amendment - Due Process",
            "provision": "No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.",
            "article": "Amendment XIV, Section 1"
        }
    ],
    "Criminal Law": [
        {
            "title": "18 U.S.C. § 371 - Conspiracy",
            "provision": "If two or more persons conspire either to commit any offense against the United States, or to defraud the United States, or any agency thereof in any manner or for any purpose, and one or more of such persons do any act to effect the object of the conspiracy, each shall be fined under this title or imprisoned not more than five years, or both.",
            "article": "18 U.S.C. § 371"
        },
        {
            "title": "18 U.S.C. § 1341 - Mail Fraud",
            "provision": "Whoever, having devised or intending to devise any scheme or artifice to defraud, or for obtaining money or property by means of false or fraudulent pretenses, representations, or promises... uses or causes to be used any facility of interstate or foreign commerce, including any facility of a national securities exchange, with intent to execute such scheme or artifice, shall be fined not more than $1,000,000 or imprisoned not more than 30 years, or both.",
            "article": "18 U.S.C. § 1341"
        },
        {
            "title": "18 U.S.C. § 1343 - Wire Fraud",
            "provision": "Whoever, having devised or intending to devise any scheme or artifice to defraud, or for obtaining money or property by means of false or fraudulent pretenses, representations, or promises, transmits or causes to be transmitted by means of wire, radio, or television communication in interstate or foreign commerce, any writings, signs, signals, pictures, or sounds for the purpose of executing such scheme or artifice, shall be fined under this title or imprisoned not more than 20 years, or both.",
            "article": "18 U.S.C. § 1343"
        }
    ],
    "Civil Rights": [
        {
            "title": "42 U.S.C. § 1983 - Civil Rights Action",
            "provision": "Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within the jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.",
            "article": "42 U.S.C. § 1983"
        },
        {
            "title": "Title VII of Civil Rights Act",
            "provision": "It shall be an unlawful employment practice for an employer to fail or refuse to hire or to discharge any individual, or otherwise to discriminate against any individual with respect to his compensation, terms, conditions, or privileges of employment, because of such individual's race, color, religion, sex, or national origin.",
            "article": "42 U.S.C. § 2000e-2"
        },
        {
            "title": "Title II of Civil Rights Act - Public Accommodations",
            "provision": "All persons shall be entitled to the full and equal enjoyment of the goods, services, facilities, and privileges, advantages, and accommodations of any place of public accommodation, as defined in this section, without discrimination or segregation on the ground of race, color, religion, or national origin.",
            "article": "42 U.S.C. § 2000a"
        }
    ],
    "Contract Law": [
        {
            "title": "Uniform Commercial Code - Good Faith",
            "provision": "Every contract or duty within this Act imposes an obligation of good faith in its performance or enforcement. 'Good faith' means honesty in fact in the conduct or transaction concerned.",
            "article": "U.C.C. § 1-304"
        },
        {
            "title": "Restatement (Second) of Contracts - Offer and Acceptance",
            "provision": "An offer is the manifestation of willingness to enter into a bargain, so made as to justify another person in understanding that his assent to that bargain is invited and will conclude it.",
            "article": "Restatement (Second) of Contracts § 24"
        }
    ],
    "Tort Law": [
        {
            "title": "Negligence - Duty of Care",
            "provision": "A person is negligent when they fail to exercise the care that a reasonably prudent person would exercise in like circumstances. The duty of care requires that individuals act with reasonable care to avoid causing harm to others.",
            "article": "Restatement (Second) of Torts § 282"
        },
        {
            "title": "Strict Liability - Defective Products",
            "provision": "One who sells any product in a defective condition unreasonably dangerous to the user or consumer or to his property is subject to liability for physical harm thereby caused to the ultimate user or consumer, or to his property, if the seller is engaged in the business of selling such a product, and it is expected to and does reach the user or consumer without substantial change in the condition in which it is sold.",
            "article": "Restatement (Second) of Torts § 402A"
        }
    ]
}

LANDMARK_CASES = [
    {
        "title": "Marbury v. Madison (1803)",
        "court": "Supreme Court of the United States",
        "summary": "Established the principle of judicial review, allowing courts to determine the constitutionality of laws.",
        "citation": "5 U.S. 137 (1803)",
        "key_holding": "The Supreme Court has the authority to review and invalidate laws that conflict with the Constitution."
    },
    {
        "title": "Brown v. Board of Education (1954)",
        "court": "Supreme Court of the United States",
        "summary": "Declared state laws establishing separate public schools for black and white students to be unconstitutional.",
        "citation": "347 U.S. 483 (1954)",
        "key_holding": "Separate educational facilities are inherently unequal, violating the Equal Protection Clause."
    },
    {
        "title": "Miranda v. Arizona (1966)",
        "court": "Supreme Court of the United States",
        "summary": "Established Miranda rights requiring law enforcement to inform suspects of their rights before custodial interrogation.",
        "citation": "384 U.S. 436 (1966)",
        "key_holding": "Suspects must be informed of their right to remain silent and right to an attorney."
    },
    {
        "title": "Roe v. Wade (1973)",
        "court": "Supreme Court of the United States",
        "summary": "Recognized a woman's constitutional right to privacy, including the right to terminate a pregnancy.",
        "citation": "410 U.S. 113 (1973)",
        "key_holding": "State laws prohibiting abortion violated the Due Process Clause of the Fourteenth Amendment."
    },
    {
        "title": "United States v. Nixon (1974)",
        "court": "Supreme Court of the United States",
        "summary": "Limited executive privilege and ordered President Nixon to turn over Watergate tapes.",
        "citation": "418 U.S. 683 (1974)",
        "key_holding": "Executive privilege is not absolute and cannot prevent production of evidence in criminal trials."
    },
    {
        "title": "Citizens United v. FEC (2010)",
        "court": "Supreme Court of the United States",
        "summary": "Held that corporate funding of independent political broadcasts in candidate elections cannot be limited.",
        "citation": "558 U.S. 310 (2010)",
        "key_holding": "Political spending by corporations, associations, and labor unions is protected free speech."
    },
    {
        "title": "Obergefell v. Hodges (2015)",
        "court": "Supreme Court of the United States",
        "summary": "Held that the fundamental right to marry is guaranteed to same-sex couples by both the Due Process Clause and the Equal Protection Clause of the Fourteenth Amendment.",
        "citation": "576 U.S. 644 (2015)",
        "key_holding": "The Constitution requires states to license and recognize marriages between two people of the same sex."
    },
    {
        "title": "Gideon v. Wainwright (1963)",
        "court": "Supreme Court of the United States",
        "summary": "Held that the Sixth Amendment's right to counsel applies to state criminal prosecutions through the Fourteenth Amendment.",
        "citation": "372 U.S. 335 (1963)",
        "key_holding": "States must provide counsel for defendants who cannot afford an attorney in criminal cases."
    },
    {
        "title": "New York Times Co. v. Sullivan (1964)",
        "court": "Supreme Court of the United States",
        "summary": "Established the actual malice standard for defamation cases involving public officials.",
        "citation": "376 U.S. 254 (1964)",
        "key_holding": "Public officials must prove actual malice (knowing falsehood or reckless disregard) to win defamation suits."
    },
    {
        "title": "Mapp v. Ohio (1961)",
        "court": "Supreme Court of the United States",
        "summary": "Held that evidence obtained in violation of the Fourth Amendment is inadmissible in state courts.",
        "citation": "367 U.S. 643 (1961)",
        "key_holding": "The exclusionary rule applies to state criminal proceedings through the Fourteenth Amendment."
    }
]


def create_provision_card(category, provision_data):
    """Create an HTML card for legal provisions"""
    return f"""
    <div class="provision-card" style="
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border-left: 4px solid #0ea5e9;
        padding: 20px;
        margin: 15px 0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: slideIn 0.5s ease-out;
    ">
        <h3 style="color: #0ea5e9; margin-top: 0; font-size: 1.3em;">{provision_data['title']}</h3>
        <p style="color: #94a3b8; font-size: 0.9em; margin: 5px 0;">{provision_data['article']}</p>
        <p style="color: #e2e8f0; line-height: 1.6; margin-top: 10px;">{provision_data['provision']}</p>
    </div>
    """


def create_case_card(case_data):
    """Create an HTML card for landmark cases"""
    return f"""
    <div class="case-card" style="
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-left: 4px solid #f59e0b;
        padding: 20px;
        margin: 15px 0;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        animation: slideIn 0.5s ease-out;
    ">
        <h3 style="color: #f59e0b; margin-top: 0; font-size: 1.3em;">{case_data['title']}</h3>
        <p style="color: #94a3b8; font-size: 0.9em; margin: 5px 0;">{case_data['court']}</p>
        <p style="color: #64748b; font-size: 0.85em; margin: 5px 0; font-style: italic;">{case_data['citation']}</p>
        <p style="color: #e2e8f0; line-height: 1.6; margin-top: 10px;"><strong>Summary:</strong> {case_data['summary']}</p>
        <p style="color: #0ea5e9; line-height: 1.6; margin-top: 10px;"><strong>Key Holding:</strong> {case_data['key_holding']}</p>
    </div>
    """


def generate_provisions_html(category=None):
    """Generate HTML for legal provisions"""
    html = "<div style='font-family: \"Segoe UI\", system-ui, sans-serif;'>"
    
    if category and category in US_LEGAL_PROVISIONS:
        provisions = US_LEGAL_PROVISIONS[category]
        html += f"<h2 style='color: #0ea5e9; margin-bottom: 20px;'>{category}</h2>"
        for provision in provisions:
            html += create_provision_card(category, provision)
    else:
        for category_name, provisions in US_LEGAL_PROVISIONS.items():
            html += f"<h2 style='color: #0ea5e9; margin-bottom: 20px; margin-top: 30px;'>{category_name}</h2>"
            for provision in provisions:
                html += create_provision_card(category_name, provision)
    
    html += "</div>"
    return html


def generate_cases_html():
    """Generate HTML for landmark cases"""
    html = "<div style='font-family: \"Segoe UI\", system-ui, sans-serif;'>"
    html += "<h2 style='color: #f59e0b; margin-bottom: 20px;'>Landmark Supreme Court Cases</h2>"
    
    for case in LANDMARK_CASES:
        html += create_case_card(case)
    
    html += "</div>"
    return html


def main(
    load_8bit: bool = False,
    base_model: str = "",
    lora_weights: str = "",
    prompt_template: str = "",
    server_name: str = "0.0.0.0",
    port: int = 7860,
    share_gradio: bool = False,
):
    base_model = base_model or os.environ.get("BASE_MODEL", "")
    assert (
        base_model
    ), "Please specify a --base_model, e.g. --base_model='huggyllama/llama-7b'"

    prompter = Prompter(prompt_template)
    tokenizer = LlamaTokenizer.from_pretrained(base_model)
    if device == "cuda":
        model = LlamaForCausalLM.from_pretrained(
            base_model,
            load_in_8bit=load_8bit,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        try:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                torch_dtype=torch.float16,
            )
        except:
            print("*"*50, "\n Attention! No Lora Weights \n", "*"*50)
    elif device == "mps":
        model = LlamaForCausalLM.from_pretrained(
            base_model,
            device_map={"": device},
            torch_dtype=torch.float16,
        )
        try:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                device_map={"": device},
                torch_dtype=torch.float16,
            )
        except:
            print("*"*50, "\n Attention! No Lora Weights \n", "*"*50)
    else:
        model = LlamaForCausalLM.from_pretrained(
            base_model, device_map={"": device}, low_cpu_mem_usage=True
        )
        try:
            model = PeftModel.from_pretrained(
                model,
                lora_weights,
                device_map={"": device},
            )
        except:
            print("*"*50, "\n Attention! No Lora Weights \n", "*"*50)

    # unwind broken decapoda-research config
    model.config.pad_token_id = tokenizer.pad_token_id = 0  # unk
    model.config.bos_token_id = 1
    model.config.eos_token_id = 2

    if not load_8bit:
        model.half()  # seems to fix bugs for some users.

    model.eval()
    if torch.__version__ >= "2" and sys.platform != "win32":
        model = torch.compile(model)

    def evaluate(
        instruction,
        temperature=0.1,
        top_p=0.75,
        top_k=40,
        num_beams=4,
        max_new_tokens=512,
        stream_output=False,
        **kwargs,
    ):
        input=None
        prompt = prompter.generate_prompt(instruction, input)
        inputs = tokenizer(prompt, return_tensors="pt")
        input_ids = inputs["input_ids"].to(device)
        generation_config = GenerationConfig(
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            num_beams=num_beams,
            **kwargs,
        )

        generate_params = {
            "input_ids": input_ids,
            "generation_config": generation_config,
            "return_dict_in_generate": True,
            "output_scores": True,
            "max_new_tokens": max_new_tokens,
        }

        if stream_output:
            def generate_with_callback(callback=None, **kwargs):
                kwargs.setdefault(
                    "stopping_criteria", transformers.StoppingCriteriaList()
                )
                kwargs["stopping_criteria"].append(
                    Stream(callback_func=callback)
                )
                with torch.no_grad():
                    model.generate(**kwargs)

            def generate_with_streaming(**kwargs):
                return Iteratorize(
                    generate_with_callback, kwargs, callback=None
                )

            with generate_with_streaming(**generate_params) as generator:
                for output in generator:
                    decoded_output = tokenizer.decode(output)
                    if output[-1] in [tokenizer.eos_token_id]:
                        break
                    yield prompter.get_response(decoded_output)
            print(decoded_output)
            return

        with torch.no_grad():
            generation_output = model.generate(
                input_ids=input_ids,
                generation_config=generation_config,
                return_dict_in_generate=True,
                output_scores=True,
                max_new_tokens=max_new_tokens,
            )
        s = generation_output.sequences[0]
        output = tokenizer.decode(s)
        print(output)
        yield prompter.get_response(output)

    # Custom CSS for legal/smart city aesthetic
    custom_css = """
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    
    .provision-card:hover, .case-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }
    
    .gradio-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        font-family: 'Segoe UI', system-ui, sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        animation: fadeIn 0.8s ease-out;
    }
    
    .main-header h1 {
        color: #0ea5e9;
        font-size: 2.5em;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    .main-header p {
        color: #94a3b8;
        font-size: 1.1em;
        margin: 10px 0 0 0;
    }
    """

    # Create the interface with tabs
    with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
        gr.HTML("""
        <div class="main-header">
            <h1>⚖️ Legal-GPT: Judicial Intelligence Platform</h1>
            <p>Advanced AI-Powered Legal Research & Analysis System | Comprehensive US Legal Provisions & Case Law Database</p>
        </div>
        """)
        
        with gr.Tabs():
            with gr.TabItem("📋 Legal Consultation"):
                with gr.Row():
                    with gr.Column(scale=1):
                        instruction_input = gr.Textbox(
                            label="Legal Query",
                            placeholder="Enter your legal question or request analysis...",
                            lines=5,
                            value=""
                        )
                        with gr.Row():
                            submit_btn = gr.Button("Analyze", variant="primary", size="lg")
                            clear_btn = gr.Button("Clear", variant="secondary")
                        
                        with gr.Accordion("⚙️ Generation Parameters", open=False):
                            temperature = gr.Slider(
                                minimum=0, maximum=1, value=0.1, step=0.1,
                                label="Temperature", info="Controls randomness"
                            )
                            top_p = gr.Slider(
                                minimum=0, maximum=1, value=0.75, step=0.05,
                                label="Top P", info="Nucleus sampling"
                            )
                            top_k = gr.Slider(
                                minimum=0, maximum=100, step=1, value=40,
                                label="Top K", info="Top-k sampling"
                            )
                            num_beams = gr.Slider(
                                minimum=1, maximum=4, step=1, value=4,
                                label="Beams", info="Number of beams for beam search"
                            )
                            max_tokens = gr.Slider(
                                minimum=50, maximum=2000, step=50, value=512,
                                label="Max Tokens", info="Maximum response length"
                            )
                            stream_output = gr.Checkbox(
                                label="Stream Output", value=True
                            )
                    
                    with gr.Column(scale=1):
                        output = gr.Textbox(
                            label="Legal Analysis",
                            lines=15,
                            interactive=False,
                            placeholder="AI-generated legal analysis will appear here..."
                        )
            
            with gr.TabItem("📜 US Legal Provisions"):
                provisions_html = generate_provisions_html()
                gr.HTML(provisions_html)
            
            with gr.TabItem("⚖️ Landmark Cases"):
                cases_html = generate_cases_html()
                gr.HTML(cases_html)
            
            with gr.TabItem("📚 About"):
                gr.Markdown("""
                # Legal-GPT: Judicial Intelligence Platform
                
                ## Overview
                
                Legal-GPT is a sophisticated AI-powered legal research and analysis platform designed to provide comprehensive legal intelligence. Built on advanced language models fine-tuned for legal applications, this platform combines cutting-edge artificial intelligence with extensive legal knowledge databases.
                
                ## Features
                
                ### 🔍 Legal Consultation
                - Interactive legal question answering
                - Case law analysis and interpretation
                - Statute explanation and application
                - Legal research assistance
                
                ### 📜 Legal Provisions Database
                - Comprehensive US Constitutional provisions
                - Federal criminal law statutes
                - Civil rights legislation
                - Administrative regulations
                
                ### ⚖️ Landmark Cases
                - Supreme Court decisions
                - Precedent analysis
                - Key legal holdings
                - Historical context
                
                ## Technology
                
                - **Base Model**: LLaMA architecture
                - **Fine-tuning**: LoRA (Low-Rank Adaptation)
                - **Framework**: PyTorch & Transformers
                - **Interface**: Gradio with custom styling
                
                ## Disclaimer
                
                **IMPORTANT**: This system is designed for educational and research purposes only. The information provided should not be construed as legal advice. Users should consult qualified legal professionals for legal advice regarding their specific circumstances.
                
                ## Terms of Use
                
                By using this platform, users acknowledge that:
                1. AI-generated content may contain errors or inaccuracies
                2. Legal interpretations require professional review
                3. The platform does not replace legal counsel
                4. Users assume responsibility for legal decisions based on platform output
                
                ---
                
                *Built with precision for legal intelligence. Powered by cutting-edge AI.*
                """)
        
        # Event handlers
        submit_btn.click(
            fn=evaluate,
            inputs=[
                instruction_input,
                temperature,
                top_p,
                top_k,
                num_beams,
                max_tokens,
                stream_output
            ],
            outputs=output
        )
        
        instruction_input.submit(
            fn=evaluate,
            inputs=[
                instruction_input,
                temperature,
                top_p,
                top_k,
                num_beams,
                max_tokens,
                stream_output
            ],
            outputs=output
        )
        
        clear_btn.click(
            fn=lambda: ("", ""),
            outputs=[instruction_input, output]
        )

    demo.queue().launch(
        server_name=server_name,
        server_port=port,
        share=share_gradio,
        show_api=False
    )


if __name__ == "__main__":
    fire.Fire(main)

