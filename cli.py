
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_input
from bot.logging_config import setup_logging
import logging

def main():
    setup_logging()

    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\n📊 Order Summary:")
        print(vars(args))

        if args.type == "MARKET":
            order = place_market_order(args.symbol, args.side, args.quantity)
        else:
            order = place_limit_order(args.symbol, args.side, args.quantity, args.price)

        print("\n✅ Order Response:")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice', 'N/A')}")

        logging.info(f"Order success: {order}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()