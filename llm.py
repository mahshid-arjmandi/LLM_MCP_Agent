from openai import AsyncOpenAI
from dotenv import load_dotenv
load_dotenv()

# ایجاد یک نمونه از کلاینت با کلید API
client = AsyncOpenAI(
    api_key=os.getenv("GAPGPT_API_KEY"),
    base_url='https://api.gapgpt.app/v1'
)
