instaGuide is a web application that automates the process of collecting, analyzing, and summarizing reviews for accommodations from Booking.com. The user enters the link of an accommodation, and the tool retrieves a large volume of reviews, enabling quick and efficient understanding of past guests' experiences.

For review extraction, the application utilizes a Web Scraper. The reviews are then processed using a Large Language Model (LLM) (Gemini 1.5 Flash), which generates a summary and provides targeted answers to user inquiries about the accommodation.

The application's backend is implemented with Django, a powerful Python web framework that ensures fast development, secure data management, and scalability. The use of Django allows seamless integration of the Web Scraper and LLM, ensuring efficient processing and presentation of information.

instaGuide provides value to both customers, who can easily access insights about an accommodation's quality without reading hundreds of reviews, and accommodation owners, who gain a better understanding of customer feedback, helping them improve their services.
