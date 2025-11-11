from openai import OpenAI
import os
os.environ["SWI_HOME_DIR"] = r"C:\Program Files\swipl"
from janus_swi import Janus

client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-5",
    input="Give me a short history of Prolog"
)

history = response.output_text
print("Facts from OpenAI: ", history)

response2 = client.responses.create(
    model="gpt-5",
    input= f"Convert the following text into prolog queries using the predicate: `history(roots, Y, Facts).` and make sure not to include any extra characters like question marks and dashes.{history}"
)
pResponse = response2.output_text.strip()
print("Facts in prolog: ", pResponse)

janus = Janus()
janus.consult_string(pResponse)
for result in janus.query("history(roots, Y, Facts)."):
    print(result)