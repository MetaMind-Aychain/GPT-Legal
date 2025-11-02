// ===== Legal Data =====
const US_LEGAL_PROVISIONS = {
    "Constitutional Law": [
        {
            title: "First Amendment",
            provision: "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.",
            article: "Amendment I"
        },
        {
            title: "Fourth Amendment",
            provision: "The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.",
            article: "Amendment IV"
        },
        {
            title: "Fifth Amendment",
            provision: "No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation.",
            article: "Amendment V"
        },
        {
            title: "Fourteenth Amendment - Due Process",
            provision: "No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.",
            article: "Amendment XIV, Section 1"
        }
    ],
    "Criminal Law": [
        {
            title: "18 U.S.C. § 371 - Conspiracy",
            provision: "If two or more persons conspire either to commit any offense against the United States, or to defraud the United States, or any agency thereof in any manner or for any purpose, and one or more of such persons do any act to effect the object of the conspiracy, each shall be fined under this title or imprisoned not more than five years, or both.",
            article: "18 U.S.C. § 371"
        },
        {
            title: "18 U.S.C. § 1341 - Mail Fraud",
            provision: "Whoever, having devised or intending to devise any scheme or artifice to defraud, or for obtaining money or property by means of false or fraudulent pretenses, representations, or promises... uses or causes to be used any facility of interstate or foreign commerce, including any facility of a national securities exchange, with intent to execute such scheme or artifice, shall be fined not more than $1,000,000 or imprisoned not more than 30 years, or both.",
            article: "18 U.S.C. § 1341"
        },
        {
            title: "18 U.S.C. § 1343 - Wire Fraud",
            provision: "Whoever, having devised or intending to devise any scheme or artifice to defraud, or for obtaining money or property by means of false or fraudulent pretenses, representations, or promises, transmits or causes to be transmitted by means of wire, radio, or television communication in interstate or foreign commerce, any writings, signs, signals, pictures, or sounds for the purpose of executing such scheme or artifice, shall be fined under this title or imprisoned not more than 20 years, or both.",
            article: "18 U.S.C. § 1343"
        }
    ],
    "Civil Rights": [
        {
            title: "42 U.S.C. § 1983 - Civil Rights Action",
            provision: "Every person who, under color of any statute, ordinance, regulation, custom, or usage, of any State or Territory or the District of Columbia, subjects, or causes to be subjected, any citizen of the United States or other person within its jurisdiction thereof to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws, shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.",
            article: "42 U.S.C. § 1983"
        },
        {
            title: "Title VII of Civil Rights Act",
            provision: "It shall be an unlawful employment practice for an employer to fail or refuse to hire or to discharge any individual, or otherwise to discriminate against any individual with respect to his compensation, terms, conditions, or privileges of employment, because of such individual's race, color, religion, sex, or national origin.",
            article: "42 U.S.C. § 2000e-2"
        },
        {
            title: "Title II of Civil Rights Act - Public Accommodations",
            provision: "All persons shall be entitled to the full and equal enjoyment of the goods, services, facilities, and privileges, advantages, and accommodations of any place of public accommodation, as defined in this section, without discrimination or segregation on the ground of race, color, religion, or national origin.",
            article: "42 U.S.C. § 2000a"
        }
    ],
    "Contract Law": [
        {
            title: "Uniform Commercial Code - Good Faith",
            provision: "Every contract or duty within this Act imposes an obligation of good faith in its performance or enforcement. 'Good faith' means honesty in fact in the conduct or transaction concerned.",
            article: "U.C.C. § 1-304"
        },
        {
            title: "Restatement (Second) of Contracts - Offer and Acceptance",
            provision: "An offer is the manifestation of willingness to enter into a bargain, so made as to justify another person in understanding that his assent to that bargain is invited and will conclude it.",
            article: "Restatement (Second) of Contracts § 24"
        }
    ],
    "Tort Law": [
        {
            title: "Negligence - Duty of Care",
            provision: "A person is negligent when they fail to exercise the care that a reasonably prudent person would exercise in like circumstances. The duty of care requires that individuals act with reasonable care to avoid causing harm to others.",
            article: "Restatement (Second) of Torts § 282"
        },
        {
            title: "Strict Liability - Defective Products",
            provision: "One who sells any product in a defective condition unreasonably dangerous to the user or consumer or to his property is subject to liability for physical harm thereby caused to the ultimate user or consumer, or to his property, if the seller is engaged in the business of selling such a product, and it is expected to and does reach the user or consumer without substantial change in the condition in which it is sold.",
            article: "Restatement (Second) of Torts § 402A"
        }
    ]
};

const LANDMARK_CASES = [
    {
        title: "Marbury v. Madison (1803)",
        court: "Supreme Court of the United States",
        summary: "Established the principle of judicial review, allowing courts to determine the constitutionality of laws.",
        citation: "5 U.S. 137 (1803)",
        keyHolding: "The Supreme Court has the authority to review and invalidate laws that conflict with the Constitution."
    },
    {
        title: "Brown v. Board of Education (1954)",
        court: "Supreme Court of the United States",
        summary: "Declared state laws establishing separate public schools for black and white students to be unconstitutional.",
        citation: "347 U.S. 483 (1954)",
        keyHolding: "Separate educational facilities are inherently unequal, violating the Equal Protection Clause."
    },
    {
        title: "Miranda v. Arizona (1966)",
        court: "Supreme Court of the United States",
        summary: "Established Miranda rights requiring law enforcement to inform suspects of their rights before custodial interrogation.",
        citation: "384 U.S. 436 (1966)",
        keyHolding: "Suspects must be informed of their right to remain silent and right to an attorney."
    },
    {
        title: "Roe v. Wade (1973)",
        court: "Supreme Court of the United States",
        summary: "Recognized a woman's constitutional right to privacy, including the right to terminate a pregnancy.",
        citation: "410 U.S. 113 (1973)",
        keyHolding: "State laws prohibiting abortion violated the Due Process Clause of the Fourteenth Amendment."
    },
    {
        title: "United States v. Nixon (1974)",
        court: "Supreme Court of the United States",
        summary: "Limited executive privilege and ordered President Nixon to turn over Watergate tapes.",
        citation: "418 U.S. 683 (1974)",
        keyHolding: "Executive privilege is not absolute and cannot prevent production of evidence in criminal trials."
    },
    {
        title: "Citizens United v. FEC (2010)",
        court: "Supreme Court of the United States",
        summary: "Held that corporate funding of independent political broadcasts in candidate elections cannot be limited.",
        citation: "558 U.S. 310 (2010)",
        keyHolding: "Political spending by corporations, associations, and labor unions is protected free speech."
    },
    {
        title: "Obergefell v. Hodges (2015)",
        court: "Supreme Court of the United States",
        summary: "Held that the fundamental right to marry is guaranteed to same-sex couples by both the Due Process Clause and the Equal Protection Clause of the Fourteenth Amendment.",
        citation: "576 U.S. 644 (2015)",
        keyHolding: "The Constitution requires states to license and recognize marriages between two people of the same sex."
    },
    {
        title: "Gideon v. Wainwright (1963)",
        court: "Supreme Court of the United States",
        summary: "Held that the Sixth Amendment's right to counsel applies to state criminal prosecutions through the Fourteenth Amendment.",
        citation: "372 U.S. 335 (1963)",
        keyHolding: "States must provide counsel for defendants who cannot afford an attorney in criminal cases."
    },
    {
        title: "New York Times Co. v. Sullivan (1964)",
        court: "Supreme Court of the United States",
        summary: "Established the actual malice standard for defamation cases involving public officials.",
        citation: "376 U.S. 254 (1964)",
        keyHolding: "Public officials must prove actual malice (knowing falsehood or reckless disregard) to win defamation suits."
    },
    {
        title: "Mapp v. Ohio (1961)",
        court: "Supreme Court of the United States",
        summary: "Held that evidence obtained in violation of the Fourth Amendment is inadmissible in state courts.",
        citation: "367 U.S. 643 (1961)",
        keyHolding: "The exclusionary rule applies to state criminal proceedings through the Fourteenth Amendment."
    }
];

// ===== Project Information =====
const PROJECT_INFO = {
    name: "Legal-GPT (AI Lawyer)",
    githubUrl: "https://github.com/MetaMind-Aychain/GPT-Legal",
    description: "Legal-GPT is a sophisticated legal language model fine-tuned on legal corpora to provide intelligent legal question answering, case analysis, and legal provision interpretation.",
    pretrainedModelsPath: "models/",
    acknowledgments: [
        {
            name: "American-LLaMA-Alpaca",
            url: "https://github.com/ymcui/American-LLaMA-Alpaca"
        },
        {
            name: "LLaMA",
            url: "https://github.com/facebookresearch/llama"
        },
        {
            name: "Alpaca",
            url: "https://github.com/tatsu-lab/stanford_alpaca"
        },
        {
            name: "alpaca-lora",
            url: "https://github.com/tloen/alpaca-lora"
        },
        {
            name: "ChatGLM-6B",
            url: "https://github.com/THUDM/ChatGLM-6B"
        },
        {
            name: "Awesome American Legal Resources",
            url: "#",
            note: "Open data resources"
        }
    ]
};

// ===== Configuration =====
const API_CONFIG = {
    baseURL: 'http://localhost:7860', // Change this to your API endpoint
    endpoint: '/api/predict' // Adjust based on your backend API
};

// ===== DOM Elements =====
const elements = {
    navLinks: document.querySelectorAll('.nav-link'),
    sections: document.querySelectorAll('.content-section'),
    consultationSection: document.getElementById('consultation'),
    provisionsSection: document.getElementById('provisions'),
    casesSection: document.getElementById('cases'),
    aboutSection: document.getElementById('about'),
    filterBtns: document.querySelectorAll('.filter-btn'),
    provisionsContainer: document.getElementById('provisions-container'),
    casesContainer: document.getElementById('cases-container'),
    loadingOverlay: document.getElementById('loading-overlay'),
    toast: document.getElementById('toast'),
    toastMessage: document.getElementById('toast-message'),
    projectContent: document.getElementById('project-content')
};

// ===== Utility Functions =====
function showToast(message, isError = false) {
    elements.toastMessage.textContent = message;
    elements.toast.classList.add('show');
    if (isError) {
        elements.toast.classList.add('error');
    } else {
        elements.toast.classList.remove('error');
    }
    
    setTimeout(() => {
        elements.toast.classList.remove('show');
    }, 3000);
}

function showLoading() {
    elements.loadingOverlay.classList.add('active');
}

function hideLoading() {
    elements.loadingOverlay.classList.remove('active');
}

// ===== Navigation =====
function initNavigation() {
    elements.navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const targetSection = link.getAttribute('data-section');
            
            // Update active nav link
            elements.navLinks.forEach(nav => nav.classList.remove('active'));
            link.classList.add('active');
            
            // Show target section
            elements.sections.forEach(section => section.classList.remove('active'));
            document.getElementById(targetSection).classList.add('active');
            
            // Scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    });
}

// ===== Project Introduction Functions =====
function renderProjectIntroduction() {
    const projectContent = document.getElementById('project-content');
    if (!projectContent) return;
    
    projectContent.innerHTML = `
        <div class="project-section">
            <div class="project-header">
                <h2>Legal-GPT: Open Source AI Legal Assistant</h2>
                <div class="github-badge">
                    <a href="${PROJECT_INFO.githubUrl}" target="_blank" class="github-link">
                        <span>🔗</span>
                        View on GitHub
                    </a>
                </div>
            </div>
            
            <div class="project-description">
                <p class="lead-text">${PROJECT_INFO.description}</p>
                <p><strong>AI Lawyer</strong> has been open-sourced and is available for testing at <a href="${PROJECT_INFO.githubUrl}" target="_blank" class="link-primary">${PROJECT_INFO.githubUrl}</a>. Pre-trained models are located in the <code>${PROJECT_INFO.pretrainedModelsPath}</code> folder.</p>
            </div>
        </div>
        
        <div class="project-section">
            <h3>🚀 Features & Capabilities</h3>
            <div class="features-list">
                <div class="feature-item">
                    <h4>Legal Question Answering</h4>
                    <p>Intelligent legal question answering powered by fine-tuned language models. The system can analyze complex legal queries and provide comprehensive responses based on legal corpora.</p>
                </div>
                <div class="feature-item">
                    <h4>Case Analysis</h4>
                    <p>Comprehensive analysis of legal cases and precedents. The model can examine case facts, identify relevant legal principles, and provide detailed case law analysis.</p>
                </div>
                <div class="feature-item">
                    <h4>Legal Provision Interpretation</h4>
                    <p>Detailed interpretation of legal provisions and statutes. The system helps users understand complex legal texts, constitutional amendments, and federal statutes.</p>
                </div>
                <div class="feature-item">
                    <h4>Multi-domain Legal Knowledge</h4>
                    <p>Coverage of multiple legal domains including constitutional law, criminal law, civil rights, contract law, tort law, and more.</p>
                </div>
            </div>
        </div>
        
        <div class="project-section">
            <h3>📊 Project Completeness & Implementation Status</h3>
            
            <div class="implementation-grid">
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Core Model</h4>
                    <p>Fine-tuned legal language model based on LLaMA architecture with LoRA (Low-Rank Adaptation) for efficient training.</p>
                </div>
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Training Pipeline</h4>
                    <p>Complete training infrastructure supporting both instruction-based fine-tuning and causal language modeling approaches.</p>
                </div>
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Inference System</h4>
                    <p>Robust inference engine with support for streaming output, configurable generation parameters, and batch processing.</p>
                </div>
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Web Interface</h4>
                    <p>Modern web interface built with Gradio, providing interactive legal consultation capabilities and legal provision browsing.</p>
                </div>
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Legal Data Integration</h4>
                    <p>Comprehensive integration of US legal provisions, landmark cases, and legal knowledge base for reference and analysis.</p>
                </div>
                <div class="impl-card completed">
                    <div class="impl-status">✅</div>
                    <h4>Pre-trained Models</h4>
                    <p>Pre-trained model weights available in the models folder, ready for deployment and further fine-tuning.</p>
                </div>
            </div>
        </div>
        
        <div class="project-section">
            <h3>🔮 Future Roadmap</h3>
            <div class="roadmap-list">
                <div class="roadmap-item">
                    <div class="roadmap-marker">🔵</div>
                    <div class="roadmap-content">
                        <h4>Enhanced Model Capabilities</h4>
                        <p>Expansion to support more legal domains, improved reasoning capabilities, and multi-lingual legal support.</p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker">🔵</div>
                    <div class="roadmap-content">
                        <h4>Real-time Legal Updates</h4>
                        <p>Integration with legal databases for real-time updates on new cases, statutes, and regulatory changes.</p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker">🔵</div>
                    <div class="roadmap-content">
                        <h4>Advanced Analytics</h4>
                        <p>Implementation of legal prediction models, case outcome analysis, and trend identification in legal systems.</p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker">🔵</div>
                    <div class="roadmap-content">
                        <h4>API Services</h4>
                        <p>Development of RESTful API services for integration with legal practice management systems and legal research platforms.</p>
                    </div>
                </div>
                <div class="roadmap-item">
                    <div class="roadmap-marker">🔵</div>
                    <div class="roadmap-content">
                        <h4>Collaborative Features</h4>
                        <p>Support for multi-user collaboration, legal document sharing, and team-based legal research workflows.</p>
                    </div>
                </div>
            </div>
        </div>
        
        <div class="project-section acknowledgments">
            <h3>🙏 Acknowledgments</h3>
            <p class="acknowledgment-intro">This project is built upon the following open-source projects. We express sincere gratitude to the related projects and developers:</p>
            
            <div class="acknowledgment-list">
                ${PROJECT_INFO.acknowledgments.map(ack => `
                    <div class="acknowledgment-item">
                        <div class="ack-icon">⭐</div>
                        <div class="ack-content">
                            <h4><a href="${ack.url}" target="_blank" class="link-primary">${ack.name}</a></h4>
                            <p><a href="${ack.url}" target="_blank" class="link-secondary">${ack.url}</a></p>
                            ${ack.note ? `<p class="ack-note">${ack.note}</p>` : ''}
                        </div>
                    </div>
                `).join('')}
            </div>
            
            <div class="acknowledgment-footer">
                <p>Additionally, this project is based on open data resources. Please refer to <strong>Awesome American Legal Resources</strong> for more information. We express our gratitude for these resources as well.</p>
            </div>
        </div>
    `;
}


// ===== Legal Provisions =====
function renderProvisions(category = 'all') {
    elements.provisionsContainer.innerHTML = '';
    
    const categories = category === 'all' 
        ? Object.keys(US_LEGAL_PROVISIONS)
        : [category];
    
    categories.forEach(cat => {
        if (!US_LEGAL_PROVISIONS[cat]) return;
        
        const categoryHeader = document.createElement('div');
        categoryHeader.className = 'category-header';
        categoryHeader.innerHTML = `<h3 style="color: var(--primary-color); font-size: 1.5rem; margin: 2rem 0 1rem 0; font-family: 'Playfair Display', serif;">${cat}</h3>`;
        elements.provisionsContainer.appendChild(categoryHeader);
        
        US_LEGAL_PROVISIONS[cat].forEach((provision, index) => {
            const card = document.createElement('div');
            card.className = 'provision-card';
            card.style.animationDelay = `${index * 0.1}s`;
            card.innerHTML = `
                <h3>${provision.title}</h3>
                <p class="article">${provision.article}</p>
                <p class="provision-text">${provision.provision}</p>
            `;
            elements.provisionsContainer.appendChild(card);
        });
    });
}

function initProvisions() {
    // Filter buttons
    elements.filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            elements.filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const category = btn.getAttribute('data-category');
            renderProvisions(category);
        });
    });
    
    // Initial render
    renderProvisions();
}

// ===== Landmark Cases =====
function renderCases() {
    elements.casesContainer.innerHTML = '';
    
    LANDMARK_CASES.forEach((caseData, index) => {
        const card = document.createElement('div');
        card.className = 'case-card';
        card.style.animationDelay = `${index * 0.1}s`;
        card.innerHTML = `
            <h3>${caseData.title}</h3>
            <p class="court">${caseData.court}</p>
            <p class="citation">${caseData.citation}</p>
            <p class="summary"><strong>Summary:</strong> ${caseData.summary}</p>
            <p class="holding"><strong>Key Holding:</strong> ${caseData.keyHolding}</p>
        `;
        elements.casesContainer.appendChild(card);
    });
}

// ===== Event Listeners =====
function initEventListeners() {
    // Event listeners are handled in individual sections
}

// ===== Initialize Application =====
function init() {
    initNavigation();
    initProvisions();
    renderCases();
    renderProjectIntroduction();
    initEventListeners();
    
    // Show initial section
    elements.consultationSection.classList.add('active');
    
    console.log('Legal-GPT initialized successfully');
}

// ===== Run on DOM Load =====
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

// ===== Smooth Scroll Polyfill =====
if (!('scrollBehavior' in document.documentElement.style)) {
    const script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/gh/cferdinandi/smooth-scroll@15/dist/smooth-scroll.polyfills.min.js';
    document.head.appendChild(script);
}

