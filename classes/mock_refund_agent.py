import logging

logger = logging.getLogger("ai-agent")

class MockRefundRequest:
    """Mock backend for local API and docker testing only"""

    async def process_message(self, user_message: str) -> str:
        logger.info("processing request with mock backend")

        return(
            "[MOCK MODE - LOCAL TESTING ONLY] "
            "The API received your message successfully. "
            "No AI model was called, and no refund was processed. "
            f"Received message: {user_message}"
        )