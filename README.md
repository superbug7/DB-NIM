# AI-Powered Data Enrichment with NVIDIA NIM

## Business Value

This project demonstrates a powerful integration between database systems and NVIDIA's NIM (NVIDIA Inference Microservices) for AI-driven data enrichment. By leveraging state-of-the-art language models, we can automatically generate high-quality, context-aware content to enhance existing data.

### Key Benefits:

1. **Automated Content Generation**: Reduce manual effort in creating product descriptions, summaries, or any text-based content.
2. **Scalability**: Process large volumes of data efficiently using NVIDIA's GPU-accelerated AI models.
3. **Improved Customer Experience**: Enhance product listings, search results, and user interfaces with AI-generated content.
4. **Data Enrichment**: Add value to existing data by augmenting it with AI-generated insights.
5. **Flexibility**: Easily adaptable to various industries and use cases, from e-commerce to content management systems.

## Technical Stack

### Current Implementation:

- **Database**: SQLite (for demonstration purposes)
- **AI Service**: NVIDIA NIM with Llama-3.1-8b-instruct model
- **Programming Language**: Python 3.8+
- **Key Libraries**: pandas, openai (for NIM API interaction)

### Strategic Partner Integration:

This solution is designed to be flexible and can easily integrate with various database systems and strategic partners. Here are some examples:

#### Teradata Integration:

To use Teradata instead of SQLite:

1. Install the Teradata Python package: pip install teradatasql
2. Replace the SQLite connection code with Teradata:
```python
import teradatasql
conn = teradatasql.connect(host="your_host", user="your_user", password="your_password", database="your_db")
```

3. Adjust SQL queries as needed to match Teradata syntax.


#### Other Strategic Data Partners:

##### Amazon Redshift: Use psycopg2 library for connection.

##### Google BigQuery: Use google-cloud-bigquery library.

##### Snowflake: Use snowflake-connector-python library.

###### Example for Snowflake:

```python
import snowflake.connector

conn = snowflake.connector.connect(
    account="your_account",
    user="your_user",
    password="your_password",
    warehouse="your_warehouse",
    database="your_database",
    schema="your_schema"
)
```

### NVIDIA NIM Integration

#### Current Cloud-based NIM:

The project uses NVIDIA's cloud-based NIM service, which provides easy access to powerful AI models without the need for local GPU infrastructure.
Downloadable NIMs (Future Enhancement):

NVIDIA plans to offer downloadable NIM containers, which will bring several additional benefits:
Data Privacy: Process sensitive data on-premises without sending it to the cloud.
Reduced Latency: Eliminate network latency for faster inference times.
Customization: Fine-tune models on your specific data for improved performance.
Cost Efficiency: Potential for reduced costs in high-volume scenarios.

#### To integrate downloadable NIMs in the future:
Set up a local GPU-enabled environment (e.g., using NVIDIA Docker).
Deploy the NIM container locally.
Update the base_url in the code to point to your local NIM endpoint.

#### Requirements

##### All required packages are listed in requirements.txt:
```
pandas==2.1.1
openai==1.3.5
```

##### For Teradata or other database integrations, add the respective library to requirements.txt.

##### Setup and Running
Clone the repository:
```
git clone https://github.com/superbug7/DB-NIM.git
cd DB-NIM
```

Install dependencies:

```
pip install -r requirements.txt
```
Set up your NVIDIA API key:

```
export NVIDIA_API_KEY=your_api_key_here
```


### Conclusion
This AI-powered data enrichment solution offers a flexible, scalable approach to enhancing your data with intelligent, context-aware content. By leveraging NVIDIA's NIM and integrating with various database systems, businesses can unlock new value in their existing data assets and improve customer experiences across multiple touchpoints.

