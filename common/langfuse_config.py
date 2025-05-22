from langfuse import Langfuse
from config import LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET

langfuse = Langfuse(
  secret_key=LANGFUSE_SECRET,
  public_key=LANGFUSE_PUBLIC_KEY,
  host=LANGFUSE_HOST
)
