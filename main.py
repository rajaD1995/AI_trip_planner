from fastapi import FastAPI
from pydantic import BaseModel  # For data validation of input from user
from agent.agentic_workflow import Graphbuilder
import os
from starlette.responses import JSONResponse
from utils.save_to_document import save_document

app = FastAPI()

class QueryRequest(BaseModel):
    # This must be linked with front end, here streamlit.
    query : str

# POST means user will give query means for some input either from Streamlit UI or HTML with Flask
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)
        graph = Graphbuilder()
        react_app = graph()  # As we use __call__ in Graphbuilder class
        # react_app = graph.build_graph()

        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png","wb") as f:
            f.write(png_graph)
        print(f"graph is saved as my_graph.png in {os.getcwd()}")

        # Assuming request is a pydantic object like {"query":"your text"}
        # first query is what we mentioned in QueryRequest and take as arg and
        # Second query is should be same as we mention in streamlit not question or any other word
        messages = {"messages":[query.query]}

        output = react_app.invoke(messages)

        # If result is in dict with messages
        if isinstance (output,dict) and "messages" in output:
            final_output = output["messages"][-1].content
            save_document(final_output)  # Saving the output in output folder
        else:
            final_output = str(output)
            save_document(final_output)  # Saving the output in output folder
        return {"answer": final_output}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error":str(e)})




