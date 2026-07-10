"""
Rule-Based AI Chatbot - Project 1
DecodeLabs - Batch 2026
Simple Version - No Dataset Required
"""

import re
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        """Initialize the chatbot with its knowledge base."""
        self.responses = {
            # Greetings
            'hello': 'Hi there! How can I help you today? ',
            'hi': 'Hello! What brings you here today?',
            'hey': 'Hey! Great to see you!',
            'good morning': 'Good morning! Hope you have a productive day! ',
            'good afternoon': 'Good afternoon! How are you doing?',
            'good evening': 'Good evening! Ready to chat? ',
            
            # Farewells
            'bye': 'Goodbye! Take care and come back anytime! ',
            'goodbye': 'See you later! It was nice chatting with you!',
            'exit': 'Exiting the conversation. Have a great day!',
            'quit': 'Quitting now. Hope to see you soon!',
            
            # Personal inquiries
            'how are you': 'I am functioning perfectly! Thanks for asking. How about you?',
            'how are you doing': 'Doing great! Just processing data and ready to assist!',
            'what is your name': 'I am DecodeBot, your very own AI assistant! ',
            'who are you': 'I am a rule-based chatbot.',
            'what can you do': 'I can answer questions, greet you, and help you explore AI concepts!',
            'tell me about yourself': 'I am a deterministic AI system built with pure if-else logic!',
            
            # AI Knowledge
            'what is ai': 'AI (Artificial Intelligence) is the simulation of human intelligence in machines.',
            'what is machine learning': 'Machine Learning is a subset of AI where systems learn from data.',
            'what is deep learning': 'Deep Learning uses neural networks to process complex patterns.',
            'what is rule based ai': 'Rule-based AI uses explicit if-else instructions for decision-making.',
            
            # Project-related
            'what is project 1': 'Project 1 is a rule-based AI chatbot foundation phase.',
            'what is decode labs': 'DecodeLabs is an AI training and development organization.',
            'why rules before learning': 'Rules provide a deterministic foundation before probabilistic learning.',
            
            # Fun
            'tell me a joke': 'Why do programmers prefer dark mode? Because light attracts bugs! ',
            'what is your purpose': 'My purpose is to help you understand AI fundamentals!',
            'who created you': 'I was created by the DecodeLabs team for the 2026 internship program.',
            'thank you': 'You\'re welcome! Always happy to help! ',
            'thanks': 'You\'re most welcome! Feel free to ask anything else.',
            
            # Time
            'what time is it': f'Current time is: {datetime.now().strftime("%I:%M %p")}',
            'what is the date': f'Today is: {datetime.now().strftime("%B %d, %Y")}',
            'what day is it': f'Today is {datetime.now().strftime("%A")}!'
        }
        
        self.exit_commands = {'bye', 'goodbye', 'exit', 'quit'}
        self.conversation_history = []
    
    def sanitize_input(self, user_input):
        """Clean up user input for better matching."""
        if not user_input:
            return ""
        
        # Convert to lowercase and strip whitespace
        sanitized = user_input.lower().strip()
        
        # Remove extra spaces
        sanitized = ' '.join(sanitized.split())
        
        # Remove punctuation (basic)
        sanitized = re.sub(r'[^\w\s]', '', sanitized)
        
        return sanitized
    
    def get_response(self, user_input):
        """Get response using dictionary lookup with .get() method."""
        # Sanitize input
        sanitized = self.sanitize_input(user_input)
        
        if not sanitized:
            return "I didn't catch that. Could you please say something? "
        
        # Log the interaction
        self.conversation_history.append({
            'time': datetime.now().strftime("%I:%M %p"),
            'user_input': user_input,
            'processed_input': sanitized
        })
        
        # Check for exit commands
        if sanitized in self.exit_commands:
            return self._handle_exit()
        
        # Check for help command
        if sanitized == 'help':
            return self._show_help()
        
        # Try keyword matching first (for flexibility)
        response = self._keyword_search(sanitized)
        
        # Use .get() method for exact matches - O(1) lookup
        if response is None:
            response = self.responses.get(sanitized)
        
        # Fallback for unknown input
        if response is None:
            response = self._handle_fallback(sanitized)
        
        return response
    
    def _keyword_search(self, sanitized):
        """Search for keywords in the input for more flexible matching."""
        keyword_map = {
            # Synonyms
            'hi': 'hello',
            'hey': 'hello',
            'howdy': 'hello',
            'morning': 'good morning',
            'afternoon': 'good afternoon',
            'evening': 'good evening',
            'how r u': 'how are you',
            'whats up': 'how are you doing',
            'sup': 'how are you doing',
            'name': 'what is your name',
            'your name': 'what is your name',
            'ai': 'what is ai',
            'artificial intelligence': 'what is ai',
            'ml': 'what is machine learning',
            'dl': 'what is deep learning',
            'joke': 'tell me a joke',
            'funny': 'tell me a joke',
            'time': 'what time is it',
            'date': 'what is the date',
            'day': 'what day is it'
        }
        
        # Check if sanitized input matches any keyword
        if sanitized in keyword_map:
            return self.responses.get(keyword_map[sanitized])
        
        # Check if any keyword is contained in the input
        for keyword, mapped in keyword_map.items():
            if keyword in sanitized:
                return self.responses.get(mapped)
        
        return None
    
    def _handle_fallback(self, sanitized):
        """Handle unknown inputs with varied fallback responses."""
        fallback_responses = [
            "I don't quite understand that. Could you rephrase? ",
            "Hmm, I'm not programmed for that yet. Let me learn about it! ",
            "I'm still learning! Can you try a different question? ",
            f"'{sanitized}' is not in my knowledge base yet. I'm growing every day! ",
            "Interesting question! I don't have an answer for that right now. ",
            "My rule-based system doesn't recognize that input. Try something else! "
        ]
        
        # Cycle through fallback responses
        fallback_index = len(self.conversation_history) % len(fallback_responses)
        return fallback_responses[fallback_index]
    
    def _handle_exit(self):
        """Handle exit commands with a proper goodbye message."""
        total_interactions = len(self.conversation_history)
        
        print("\n" + "="*50)
        print(f"📊 CONVERSATION SUMMARY")
        print("="*50)
        print(f"Total interactions: {total_interactions}")
        
        if total_interactions > 0:
            print("\n📝 Last 5 interactions:")
            for i, entry in enumerate(self.conversation_history[-5:], 1):
                print(f"  {i}. You: {entry['user_input'][:30]}...")
        
        return "\n Thanks for chatting! Remember: Rules before deep learning! Come back soon!\n"
    
    def _show_help(self):
        """Show available commands."""
        return """
 AVAILABLE COMMANDS

 GREETINGS:
hello, hi, hey, good morning, good afternoon, good evening

 FAREWELLS:
bye, goodbye, exit, quit

 PERSONAL:
how are you, what is your name, who are you, what can you do

 AI KNOWLEDGE:
what is ai, what is machine learning, what is deep learning
what is rule based ai, what is project 1

 TIME:
what time is it, what is the date, what day is it

 FUN:
tell me a joke, thank you, thanks

 TIP: Just type naturally! I'll try my best to understand!
"""
    
    def run(self):
        """Main execution loop - the heartbeat of the chatbot."""
        print("\n" + "="*60)
        print("🤖 DECODEBOT - Rule-Based AI Chatbot")
        print("="*60)
        print("Created by: DecodeLabs | Batch: 2026")
        print("Type 'help' for available commands")
        print("Type 'bye' or 'exit' to quit")
        print("="*60 + "\n")
        
        print(" DecodeBot is ready to chat!")
        print("-" * 50)
        
        while True:
            try:
                # Get user input
                user_input = input(" You: ").strip()
                
                # Check for empty input
                if not user_input:
                    print(" Bot: Please type something!\n")
                    continue
                
                # Get and display response
                response = self.get_response(user_input)
                print(f" Bot: {response}\n")
                
                # Check if we should exit
                if user_input.lower().strip() in self.exit_commands:
                    break
                
            except KeyboardInterrupt:
                print("\n\n Bot: Interrupted. Thanks for chatting! 👋")
                break
            except Exception as e:
                print(f" Bot: An error occurred: {e}")
                print(" Bot: Please try again.\n")


# Main execution
if __name__ == "__main__":
    # Create and run the chatbot
    bot = RuleBasedChatbot()
    bot.run()