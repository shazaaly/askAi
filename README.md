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

## Dataset intents tell now:
['ask_about_app', 'ask_about_loyalty_coins', 'ask_delivery_options', 'ask_for_change_delivery_date', 'ask_for_product_recommendations', 'ask_nutrition_facts', 'ask_pricing_policy', 'ask_product_description', 'ask_product_discounts', 'ask_product_price', 'ask_return_policy', 'ask_shipping_fees', 'check_shipping_status', 'check_stock_availability', 'compare_prices', 'compare_products', 'find_similar_products', 'how_to_contact_support', 'how_to_get_an_offer', 'how_to_place_order', 'how_to_store_product', 'how_to_use_product', 'out_of_scope', 'request_customer_support', 'suggest_cheaper_alternative', 'track_order_status']



## Run Script
```python
 python upload_dataset.py

## 🛠 How to Load

```python
from datasets import load_dataset

dataset = load_dataset("ShazaAly/suplyd-arabic-intents-dataset-v1")
print(dataset["train"][0])
