#!/usr/bin/env python3
"""Document Search Engine CLI."""
import argparse
from pathlib import Path
from search_engine import DocumentSearchEngine


def main():
    parser = argparse.ArgumentParser(description="Local document search")
    parser.add_argument("--index", default="doc_index.json", help="Index file")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    index_cmd = subparsers.add_parser("index", help="Index documents")
    index_cmd.add_argument("directory")
    index_cmd.add_argument("-e", "--extensions", nargs="+", default=[".txt", ".md"])
    
    search_cmd = subparsers.add_parser("search", help="Search documents")
    search_cmd.add_argument("query")
    search_cmd.add_argument("-n", "--limit", type=int, default=10)
    
    args = parser.parse_args()
    engine = DocumentSearchEngine(Path(args.index))
    
    try:
        if args.command == "index":
            print(f"Indexing {args.directory}...")
            engine.index_directory(Path(args.directory), args.extensions)
            print(f"✓ Indexed {len(engine.index)} documents")
        
        elif args.command == "search":
            results = engine.search(args.query, args.limit)
            
            if not results:
                print("No results found")
            else:
                print(f"Found {len(results)} results:\n")
                for i, result in enumerate(results, 1):
                    print(f"{i}. {result['path']} (score: {result['score']})")
                    print(f"   {result['preview'][:100]}...\n")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
