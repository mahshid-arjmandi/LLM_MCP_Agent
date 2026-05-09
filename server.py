from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Demo",json_response=True)

@mcp.tool()
def sum_numbers(a:int,b:int)->int:
    return a+b

if __name__ == "__main__":
    print("MCP server started...")
    mcp.run()
