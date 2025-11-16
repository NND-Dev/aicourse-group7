"""AI-Centric Travel Planning CLI.

New simplified flow:
1. Enter API key securely
2. Start conversation with AI
3. AI guides through: preferences → destinations → activities → dates/weather → plan
"""

import sys
import getpass
from datetime import datetime
from colorama import Fore, Style, init as colorama_init
from openai import OpenAI

# Initialize colorama
colorama_init(autoreset=True)


class AITravelCLI:
    """AI-Driven Travel Planning CLI."""
    
    def __init__(self):
        """Initialize CLI."""
        self.running = True
        self.api_key = None
        self.client = None
        self.conversation_history = []
        self.base_url = "https://aiportalapi.stu-platform.live/jpe"
        self.model = "GPT-5-mini"
        
        # Travel context
        self.user_preferences = {}
        self.selected_destination = None
        self.selected_activities = []
        self.travel_dates = None
    
    def run(self):
        """Start the application."""
        self.print_welcome()
        
        # Step 1: Get API key
        if not self.setup_api_key():
            print(f"{Fore.RED}Cannot proceed without API key. Exiting...{Style.RESET_ALL}")
            return
        
        # Step 2: Main loop
        while self.running:
            try:
                self.print_menu()
                choice = input(f"\n{Fore.YELLOW}Enter your choice: {Style.RESET_ALL}").strip()
                self.handle_choice(choice)
            
            except KeyboardInterrupt:
                print(f"\n\n{Fore.YELLOW}Interrupted by user{Style.RESET_ALL}")
                self.running = False
            
            except Exception as e:
                print(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
        
        self.print_goodbye()
    
    def print_welcome(self):
        """Print welcome banner."""
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}✈️   AI Travel Planner - Your Intelligent Travel Assistant   🌍{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}Let AI help you plan the perfect trip!{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Powered by OpenAI GPT-5-mini{Style.RESET_ALL}\n")
    
    def setup_api_key(self) -> bool:
        """Securely get API key from user."""
        print(f"\n{Fore.CYAN}🔑 API Key Setup{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'─'*70}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}To use this application, you need an OpenAI API key.{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Get your key from: {Fore.BLUE}https://aiportalapi.stu-platform.live/jpe{Style.RESET_ALL}")
        print(f"{Fore.WHITE}{'─'*70}{Style.RESET_ALL}\n")
        
        # Get API key (try hidden input first, fallback to visible)
        try:
            api_key = getpass.getpass(f"{Fore.YELLOW}Enter your API key (hidden): {Style.RESET_ALL}").strip()
        except Exception:
            # Fallback to visible input if getpass fails
            api_key = input(f"{Fore.YELLOW}Enter your API key: {Style.RESET_ALL}").strip()
        
        if not api_key:
            print(f"{Fore.RED}❌ API key is required!{Style.RESET_ALL}")
            return False
        
        # Validate key format
        if not api_key.startswith('sk-'):
            print(f"{Fore.RED}❌ Invalid key format. Key should start with 'sk-'{Style.RESET_ALL}")
            return False
        
        # Skip validation, just set the API key
        # API key will be validated on first actual use
        print(f"\n{Fore.GREEN}✅ API key accepted!{Style.RESET_ALL}\n")
        
        try:
            # Create client without testing
            self.api_key = api_key
            self.client = OpenAI(
                api_key=api_key,
                base_url=self.base_url
            )
            return True
        
        except Exception as e:
            print(f"{Fore.RED}❌ Failed to create OpenAI client: {str(e)}{Style.RESET_ALL}")
            return False
    
    def print_menu(self):
        """Print simplified menu."""
        print(f"\n{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Main Menu:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1. 🚀 Start Planning (Chat with AI){Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. 🚪 Exit{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'─'*70}{Style.RESET_ALL}")
    
    def handle_choice(self, choice: str):
        """Handle menu choice."""
        if choice == "1":
            self.start_planning()
        elif choice == "2":
            self.running = False
        else:
            print(f"{Fore.RED}Invalid choice. Please enter 1 or 2.{Style.RESET_ALL}")
    
    def start_planning(self):
        """Start AI-guided travel planning conversation."""
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}🚀 AI Travel Planning Assistant{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.WHITE}I'll help you plan your perfect trip!{Style.RESET_ALL}")
        print(f"{Fore.WHITE}Type 'back' anytime to return to main menu.{Style.RESET_ALL}\n")
        
        # Reset context
        self.conversation_history = []
        self.user_preferences = {}
        
        # Initial AI greeting
        greeting = self._chat_with_ai(
            """You are an expert travel planning assistant. Greet the user warmly and ask them:
1. Where would they like to travel? (or if they're not sure, what kind of place they're interested in)
2. What are their travel preferences? (budget level, interests like beach/culture/food/adventure, etc.)

Be friendly and conversational. Keep it brief (2-3 sentences).""",
            system_message=True
        )
        
        print(f"{Fore.GREEN}🤖 AI Assistant:{Style.RESET_ALL} {greeting}\n")
        
        # Conversation loop
        planning_stage = "preferences"  # preferences → destination → activities → dates → plan
        
        while True:
            user_input = input(f"{Fore.YELLOW}You: {Style.RESET_ALL}").strip()
            
            if user_input.lower() in ['back', 'exit', 'quit']:
                print(f"\n{Fore.CYAN}Returning to main menu...{Style.RESET_ALL}")
                break
            
            if not user_input:
                continue
            
            # Get AI response based on current stage
            ai_response = self._intelligent_response(user_input, planning_stage)
            
            print(f"\n{Fore.GREEN}🤖 AI Assistant:{Style.RESET_ALL} {ai_response}\n")
            
            # Update planning stage based on conversation
            planning_stage = self._determine_next_stage(ai_response, planning_stage)
    
    def _chat_with_ai(self, user_message: str, system_message: bool = False) -> str:
        """Send message to AI and get response."""
        try:
            # Build messages
            messages = [
                {
                    "role": "system",
                    "content": """You are an expert travel planning assistant. You help users:
1. Discover destinations based on their preferences
2. Suggest activities and attractions
3. Check weather and best times to visit
4. Create detailed travel itineraries

Be conversational, friendly, and provide specific, actionable advice.
When suggesting destinations or activities, include:
- Why it's a good match for their preferences
- Estimated costs
- Best times to visit
- Weather considerations
- Practical tips"""
                }
            ]
            
            # Add conversation history
            messages.extend(self.conversation_history)
            
            # Add current message
            role = "system" if system_message else "user"
            messages.append({"role": role, "content": user_message})
            
            # Call API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=2000,  # Increased for GPT-5 reasoning + response
                temperature=1.0,  # GPT-5 only supports temperature=1
                timeout=30.0  # 30 second timeout
            )
            
            if not response.choices:
                return "API returned no response. Please check your model name or API configuration."
            
            ai_message = response.choices[0].message.content
            
            if not ai_message:
                return "I'm having trouble generating a response. Please try again."
            
            # Update history (only user messages and AI responses, not system)
            if not system_message:
                self.conversation_history.append({"role": "user", "content": user_message})
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            
            return ai_message
        
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def _intelligent_response(self, user_input: str, stage: str) -> str:
        """Generate AI response based on conversation stage."""
        # Add stage context to help AI understand where we are in the planning
        stage_prompts = {
            "preferences": "The user is sharing their travel preferences. Help them clarify what they're looking for.",
            "destination": "Help the user choose a destination based on their preferences. Provide 2-3 specific suggestions with reasons.",
            "activities": "Suggest specific activities and attractions for their chosen destination. Include costs and time needed.",
            "dates": "Ask about their travel dates and provide weather information and seasonal advice for their destination.",
            "plan": "Create a detailed itinerary with day-by-day breakdown, estimated costs, and practical tips."
        }
        
        context = f"\n\n[Planning Stage: {stage}. {stage_prompts.get(stage, '')}]"
        
        return self._chat_with_ai(user_input + context)
    
    def _determine_next_stage(self, ai_response: str, current_stage: str) -> str:
        """Determine next planning stage based on conversation."""
        # Simple keyword-based stage detection
        response_lower = ai_response.lower()
        
        if current_stage == "preferences":
            if any(word in response_lower for word in ["suggest", "recommend", "consider", "destination"]):
                return "destination"
        
        elif current_stage == "destination":
            if any(word in response_lower for word in ["activities", "things to do", "attractions", "visit"]):
                return "activities"
        
        elif current_stage == "activities":
            if any(word in response_lower for word in ["when", "dates", "weather", "season", "time"]):
                return "dates"
        
        elif current_stage == "dates":
            if any(word in response_lower for word in ["itinerary", "plan", "schedule", "day-by-day"]):
                return "plan"
        
        return current_stage
    
    def print_goodbye(self):
        """Print goodbye message."""
        print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}✈️  Thank you for using AI Travel Planner!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Safe travels and amazing adventures! 🌍{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")


def main():
    """Entry point for AI Travel CLI."""
    cli = AITravelCLI()
    cli.run()


if __name__ == "__main__":
    main()
