
from services.ai.gemini_client import GeminiAIClient
from utils.logger import logger



def main():
    #logger.info("Starting NetworkGPT...")

    
    client = GeminiAIClient()
    response = client.generate_text("Expalin about AAA in networking with real life example in 5 lines")
    print("\n responce from gemini: \n", response)
    #logger.success("Gemini AI Client created successfully.")


if __name__ == "__main__":
    main()