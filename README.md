# Suplyd Arabic Intents Dataset v1

A labeled dataset of Arabic user utterances for training and evaluating intent classification models in the context of e-commerce and product inquiries. The dataset includes both colloquial Egyptian Arabic and English examples, covering 27 different intent categories.

## 💡 Use Case

This dataset is ideal for building:

- AI customer support agents
- Product search assistants
- Multilingual intent classifiers
- RAG-based product query systems

## 📊 Dataset Details

- **Language:** Arabic (mainly Egyptian dialect) and English
- **Total Samples:** 3,050
- **Intents:** 27 distinct labels
- **Format:** CSV, converted to Hugging Face `datasets` format
- **Columns:**
  - `text`: the user utterance
  - `label`: the corresponding intent (e.g., `ask_product_price`, `check_stock_availability`)

## 📚 Intent Examples

| Intent                  | Example (text)                                  |
|-------------------------|--------------------------------------------------|
| ask_product_description | ممكن تفاصيل عن المنتج ده؟                       |
| ask_product_price       | بكم سعر العصير دا؟                              |
| check_stock_availability | هل المنتج ده متوفر في المخزن؟                  |

## 🛠 How to Load

```python
from datasets import load_dataset

dataset = load_dataset("ShazaAly/suplyd-arabic-intents-dataset-v1")
print(dataset["train"][0])
