from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from utils.models_loaders import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT



class Graphbuilder():
    def __init__(self):
        self.model_loader = ModelLoader()
        self.llm = self.model_loader.load_llm()

        self.tools = []

        self.weather_tools = 

    def agent_function(self,state:MessagesState):
        '''Main agent function. It will take decesion'''
        user_question = state["messages"]
        input_question = [self.SYSTEM_PROMPT] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {"messages":[response]}

    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent",self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()

        return self.graph

    def __call__(self):
        return self.build_graph()
