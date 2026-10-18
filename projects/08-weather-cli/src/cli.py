#!/usr/bin/env python3
"""Weather CLI."""
import argparse
from pathlib import Path
from weather_client import WeatherClient


def main():
    parser = argparse.ArgumentParser(description="Weather CLI")
    parser.add_argument("--lat", type=float, help="Latitude")
    parser.add_argument("--lon", type=float, help="Longitude")
    parser.add_argument("--demo", action="store_true", help="Use offline sample")
    parser.add_argument("--save-sample", help="Save sample response to file")
    
    args = parser.parse_args()
    
    try:
        client = WeatherClient()
        
        if args.save_sample:
            client.save_sample_response(Path(args.save_sample))
            print(f"✓ Saved sample to {args.save_sample}")
            return 0
        
        if args.demo:
            # Use bundled or saved sample
            sample_path = Path(__file__).parent / "sample_response.json"
            if not sample_path.exists():
                client.save_sample_response(sample_path)
            data = client.load_offline_sample(sample_path)
            print("[DEMO MODE - Offline sample data]\n")
        else:
            if not args.lat or not args.lon:
                print("Error: --lat and --lon required (or use --demo)")
                return 1
            data = client.get_weather(args.lat, args.lon)
        
        print(client.format_weather(data))
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
