# LLM_MCP_Agent
A professional-grade AI Agent implementation using Model Context Protocol (MCP) for dynamic tool discovery and execution. Built with Python and GapGPT (GPT-gpt-4o).
Demo MCP Server

Python

MCP

License

A simple Model Context Protocol (MCP) server built with Python using FastMCP.

This project demonstrates how to expose custom tools that AI clients (such as Claude Desktop or other MCP-compatible apps) can call.
Overview

This MCP server provides a single tool:

sum_numbers – returns the sum of two integers.

The project is meant as a minimal example for learning how to build MCP tools and servers.
Features

    Simple MCP server implementation
    Tool definition using decorators
    JSON responses enabled
    Easy to extend with more tools

Project Structure

                                                                    text
demo-mcp-server
│
├─ server.py
└─ README.md

Installation

Clone the repository:

                                                                    bash
git clone https://github.com/your-username/demo-mcp-server.git
cd demo-mcp-server

Install dependencies:

                                                                    bash
pip install mcp

Running the Server

Start the MCP server:

                                                                    bash
python server.py

Terminal output:

                                                                    text
MCP server started...

The server will now be ready to receive MCP tool calls.
Example Code

                                                                    python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo", json_response=True)

@mcp.tool()
def sum_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print("MCP server started...")
    mcp.run()

Available Tools
sum_numbers

Adds two integers.

Parameters:

    a (int) – first number
    b (int) – second number

Example call:

                                                                    text
sum_numbers(a=3, b=5)

Response:

                                                                    text
8

Using with Claude Desktop (Example)

Example MCP configuration:

                                                                    text
{
  "mcpServers": {
    "demo-server": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}

After adding this configuration, restart Claude Desktop and the tool will appear automatically.
Extending the Server

You can easily add more tools:

                                                                    python
@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b
