# Legal-GPT: Advanced Legal Language Model

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/MetaMind-Aychain/GPT-Legal)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Overview

Legal-GPT (AI Lawyer) is a sophisticated open-source legal language model fine-tuned on legal corpora to provide intelligent legal question answering, case analysis, and legal provision interpretation. Built on top of LLaMA architectures with LoRA (Low-Rank Adaptation) fine-tuning, this system delivers precise legal insights with computational efficiency.

**🎉 This project is now open-source!** Pre-trained models are available in the `models/` folder. You can test the system by visiting [https://github.com/MetaMind-Aychain/GPT-Legal](https://github.com/MetaMind-Aychain/GPT-Legal).

## Project Status

✅ **Core Model**: Fine-tuned legal language model based on LLaMA architecture with LoRA  
✅ **Training Pipeline**: Complete training infrastructure supporting instruction-based and causal language modeling  
✅ **Inference System**: Robust inference engine with streaming support and configurable parameters  
✅ **Web Interface**: Modern web interface built with Gradio and static HTML/CSS/JS  
✅ **Legal Data Integration**: Comprehensive integration of US legal provisions and landmark cases  
✅ **Pre-trained Models**: Model weights available in the `models/` folder for deployment

## Quick Start

```bash
# Clone the repository
git clone https://github.com/MetaMind-Aychain/GPT-Legal.git
cd GPT-Legal

# Install dependencies
pip install -r requirements.txt

# Pre-trained models are located in the models/ folder
# Use webapp.py to launch the enhanced web interface
python webapp.py --base_model=models/base_models/your_model --lora_weights=models/lora_weights/your_lora
```

## Features

- **Advanced Legal Q&A**: Interactive legal question answering powered by fine-tuned language models
- **Case Analysis**: Comprehensive analysis of legal cases and precedents
- **Statute Interpretation**: Detailed interpretation of legal provisions and statutes
- **LoRA Fine-tuning**: Efficient parameter-efficient fine-tuning using Low-Rank Adaptation
- **Flexible Training**: Support for both instruction-based and causal language modeling training
- **Web Interface**: Professional web interface with legal documentation display
- **Multi-device Support**: Optimized for CUDA, MPS, and CPU inference

## Architecture

### Core Components

1. **Base Model**: Built on LLaMA architecture with configurable base models
2. **LoRA Adapters**: Parameter-efficient fine-tuning using Low-Rank Adaptation
3. **Prompt Templates**: Flexible template system for various legal tasks
4. **Inference Engine**: Optimized inference with streaming support
5. **Web UI**: Gradio-based interface for interactive legal consultations

### Technical Stack

- **Deep Learning Framework**: PyTorch
- **Transformer Library**: Hugging Face Transformers
- **Fine-tuning**: PEFT (Parameter-Efficient Fine-Tuning)
- **Web Interface**: Gradio
- **Data Processing**: Hugging Face Datasets

## Installation

### Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended) or CPU
- 16GB+ RAM (32GB+ recommended for training)
- PyTorch installed

### Step 1: Clone the Repository

```bash
git clone https://github.com/MetaMind-Aychain/GPT-Legal.git
cd GPT-Legal
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Prepare Base Model

Download and prepare your base LLaMA model:

```bash
# Place your base model in models/base_models/
mkdir -p models/base_models
# Follow Hugging Face model loading instructions

# Or use pre-trained models from the models/ folder
# Pre-trained model weights are available in models/lora_weights/
```

## Usage

### Training

#### Instruction-Based Fine-tuning

Fine-tune the model on legal instruction datasets:

```bash
python finetune.py \
    --base_model=models/base_models/llama-7b \
    --data_path=./data/legal_instructions.json \
    --output_dir=./outputs/legal-llama-lora \
    --num_epochs=3 \
    --batch_size=128 \
    --micro_batch_size=4 \
    --learning_rate=3e-4 \
    --cutoff_len=512 \
    --lora_r=8 \
    --lora_alpha=16 \
    --prompt_template_name=alpaca
```

#### Causal Language Modeling

Train on continuous legal text data:

```bash
python train_clm.py \
    --base_model=models/base_models/llama-7b \
    --data_path=./data/legal_texts.json \
    --output_dir=./outputs/legal-llama-clm \
    --num_epochs=10 \
    --batch_size=128 \
    --micro_batch_size=4 \
    --learning_rate=3e-4 \
    --cutoff_len=512 \
    --lora_r=8 \
    --lora_alpha=16
```

### Inference

#### Interactive Inference

```bash
python infer.py \
    --base_model=models/base_models/llama-7b \
    --lora_weights=./outputs/legal-llama-lora \
    --prompt_template=alpaca \
    --infer_data_path=./resources/example_infer_data.json
```

#### Batch Inference from File

The inference script supports both file-based and interactive modes:

```bash
python infer.py \
    --base_model=models/base_models/llama-7b \
    --lora_weights=./outputs/legal-llama-lora \
    --infer_data_path=./resources/example_infer_data.json
```

### Web Interface

Launch the professional web interface:

```bash
python webui.py \
    --base_model=models/base_models/llama-7b \
    --lora_weights=./outputs/legal-llama-lora \
    --prompt_template=alpaca \
    --server_name=0.0.0.0 \
    --share_gradio=False
```

Access the interface at `http://localhost:7860` (or the displayed URL).

For the enhanced web interface with US legal provisions and cases:

```bash
python webapp.py \
    --base_model=models/base_models/llama-7b \
    --lora_weights=./outputs/legal-llama-lora \
    --server_name=0.0.0.0 \
    --port=7860
```

## Data Format

### Instruction-Based Training Data

```json
{
    "instruction": "Explain the concept of mens rea in criminal law.",
    "input": "",
    "output": "Mens rea, Latin for 'guilty mind', refers to the mental state requirement in criminal law..."
}
```

### Causal Language Modeling Data

```json
{
    "content": "The United States Constitution establishes the framework for federal law enforcement..."
}
```

## Configuration

### LoRA Hyperparameters

- `lora_r`: Rank of the low-rank adaptation (default: 8)
- `lora_alpha`: Scaling factor (default: 16)
- `lora_dropout`: Dropout rate (default: 0.05)
- `lora_target_modules`: Target modules for adaptation (default: ["q_proj", "v_proj"])

### Training Hyperparameters

- `batch_size`: Total batch size (default: 128)
- `micro_batch_size`: Micro batch size per device (default: 4)
- `num_epochs`: Number of training epochs (default: 3)
- `learning_rate`: Learning rate (default: 3e-4)
- `cutoff_len`: Maximum sequence length (default: 512)

### Inference Parameters

- `temperature`: Sampling temperature (default: 0.1)
- `top_p`: Nucleus sampling parameter (default: 0.75)
- `top_k`: Top-k sampling parameter (default: 40)
- `num_beams`: Number of beams for beam search (default: 1-4)
- `max_new_tokens`: Maximum tokens to generate (default: 256)

## Project Structure

```
Legal-GPT/
├── assets/                 # Static assets (logos, demos)
├── data/                   # Training and validation data
├── models/
│   ├── base_models/       # Base model directories
│   └── lora_weights/      # Fine-tuned LoRA adapters (pre-trained models available here)
├── outputs/               # Training outputs and checkpoints
├── resources/             # Resource files (vocabularies, examples)
├── scripts/               # Training and inference scripts
├── static/                # Static web frontend (HTML, CSS, JS)
│   ├── index.html        # Main frontend interface
│   ├── styles.css        # Stylesheet
│   └── app.js            # JavaScript logic
├── templates/             # Prompt templates
├── tools/                 # Utility tools
├── utils/                 # Utility modules
├── finetune.py           # Instruction-based fine-tuning
├── train_clm.py          # Causal language modeling training
├── infer.py              # Inference script
├── webui.py              # Basic Gradio web interface
├── webapp.py             # Enhanced web application (Gradio)
└── requirements.txt      # Python dependencies
```

## Legal Provisions and Cases

The enhanced web interface includes comprehensive displays of:

- **United States Constitution**: Full text with article-by-article navigation
- **Federal Statutes**: Key provisions from US Code
- **Landmark Cases**: Analysis of significant Supreme Court decisions
- **Legal Precedents**: Important case law references
- **Statutory Interpretation**: Detailed explanations of legal provisions

### Example Legal Topics Covered

- Constitutional Law
- Criminal Law and Procedure
- Civil Rights and Liberties
- Contract Law
- Tort Law
- Property Law
- Corporate Law
- Intellectual Property
- Administrative Law
- International Law

## Advanced Features

### Model Merging

Merge LoRA adapters with base models:

```bash
python merge.py \
    --base_model=models/base_models/llama-7b \
    --lora_weights=./outputs/legal-llama-lora \
    --output_dir=./outputs/merged-model
```

### Evaluation

Evaluate model performance:

```python
from utils.evaluate import evaluate_model

results = evaluate_model(
    model_path="./outputs/legal-llama-lora",
    test_data="./data/test_set.json"
)
```

## Performance Optimization

### Memory Optimization

- Enable 8-bit quantization for training:
  ```bash
  python finetune.py --load_8bit=True ...
  ```

- Use gradient checkpointing for larger models
- Implement gradient accumulation for effective larger batch sizes

### Speed Optimization

- Enable torch.compile (PyTorch 2.0+):
  ```python
  model = torch.compile(model)
  ```

- Use mixed precision training (FP16)
- Optimize batch sizes for your hardware

## Future Roadmap

The following features are planned for future development:

- **Enhanced Model Capabilities**: Expansion to support more legal domains, improved reasoning capabilities, and multi-lingual legal support
- **Real-time Legal Updates**: Integration with legal databases for real-time updates on new cases, statutes, and regulatory changes
- **Advanced Analytics**: Implementation of legal prediction models, case outcome analysis, and trend identification in legal systems
- **API Services**: Development of RESTful API services for integration with legal practice management systems and legal research platforms
- **Collaborative Features**: Support for multi-user collaboration, legal document sharing, and team-based legal research workflows

## Best Practices

1. **Data Quality**: Ensure high-quality, diverse legal training data
2. **Prompt Engineering**: Design effective prompts for your use case
3. **Hyperparameter Tuning**: Experiment with LoRA ranks and learning rates
4. **Validation**: Use validation sets to monitor training progress
5. **Ethical Considerations**: Always include disclaimers about AI legal advice

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

**IMPORTANT LEGAL NOTICE**: This system is designed for educational and research purposes only. The information provided by this system should not be construed as legal advice. Users should consult qualified legal professionals for legal advice regarding their specific circumstances. The developers and contributors are not responsible for any legal consequences arising from the use of this system.

## Citation

If you use Legal-GPT in your research, please cite:

```bibtex
@software{legal_gpt,
  title={Legal-GPT: Advanced Legal Language Model},
  author={Legal-GPT Contributors},
  year={2024},
  url={https://github.com/MetaMind-Aychain/GPT-Legal}
}
```

## Support

For questions, issues, or contributions, please:

- Open an issue on GitHub
- Contact the maintainers
- Check existing documentation and examples

## Acknowledgments

This project is built upon the following open-source projects. We express sincere gratitude to the related projects and developers:

### Open Source Projects

- **[Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)**: Chinese LLaMA & Alpaca LLMs
- **[LLaMA](https://github.com/facebookresearch/llama)**: Meta AI's LLaMA language model
- **[Alpaca](https://github.com/tatsu-lab/stanford_alpaca)**: Stanford Alpaca instruction-following language model
- **[alpaca-lora](https://github.com/tloen/alpaca-lora)**: LoRA implementation for Alpaca
- **[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)**: ChatGLM-6B: An Open Bilingual Dialogue Language Model

### Data Resources

Additionally, this project is based on open data resources. Please refer to **Awesome American Legal Resources** for more information. We express our gratitude for these resources as well.

### Libraries and Frameworks

- **[Hugging Face](https://huggingface.co/)**: Transformers and PEFT libraries
- **Meta AI**: LLaMA architecture
- **PyTorch**: Deep learning framework
- **Gradio**: Web interface framework

### Community

- The open-source legal data community
- All contributors and users of this project

We thank all the developers, researchers, and contributors who have made these excellent tools and resources available to the community.

---

**Built with precision for legal intelligence. Powered by cutting-edge AI.**

