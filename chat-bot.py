import tkinter as tk
from tkinter import scrolledtext, messagebox
import random

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ SparkBot ✨")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(True, True)
        
        self.colors = {
            "bg": "#2c3e50",
            "bot_bubble": "#3498db",
            "user_bubble": "#2ecc71",
            "text": "#ecf0f1",
            "input_bg": "#34495e",
            "button_bg": "#9b59b6"
        }
        
        self.responses = {
            "greeting": ["Hi there! 👋", "Hello! Nice to see you!", "Hey! How can I help you today?"],
            "howareyou": ["I'm feeling great! Thanks for asking! 😊", "Doing awesome! Ready to chat!", "I'm excellent! How about you?"],
            "bye": ["Goodbye! Take care! 🌟", "See you later! 👋", "Bye! Have a wonderful day!"],
            "name": ["I'm SparkBot! Your cheerful assistant! 🤖", "They call me SparkBot! Ready to spark conversations!"],
            "joke": ["Why don't scientists trust atoms? Because they make up everything! 😄",
                     "What do you call a bear with no teeth? A gummy bear! 🐻"],
            "love": ["You're awesome! ❤️", "Sending virtual hugs! 🤗", "You make this conversation special!"],
            "weather": ["I'd check the weather for you, but I don't have a window! 😅",
                       "I'm always sunny inside this computer! ☀️"],
            "help": ["Try asking me about my name, tell me a joke, or just say hello!"]
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        header = tk.Frame(self.root, bg=self.colors["bot_bubble"], height=60)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title_label = tk.Label(header, text="💬 SparkBot Chat", font=("Arial", 18, "bold"),
                              bg=self.colors["bot_bubble"], fg=self.colors["text"])
        title_label.pack(pady=15)
        
        self.chat_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.chat_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)
        
        self.chat_area = scrolledtext.ScrolledText(self.chat_frame, wrap=tk.WORD,
                                                  bg=self.colors["input_bg"], fg=self.colors["text"],
                                                  font=("Arial", 11), relief=tk.FLAT, bd=2)
        self.chat_area.pack(fill=tk.BOTH, expand=True)
        self.chat_area.tag_configure("bot", foreground=self.colors["bot_bubble"], font=("Arial", 10, "bold"))
        self.chat_area.tag_configure("user", foreground=self.colors["user_bubble"], font=("Arial", 10, "bold"))
        self.chat_area.configure(state=tk.DISABLED)
        
        input_frame = tk.Frame(self.root, bg=self.colors["bg"])
        input_frame.pack(fill=tk.X, padx=15, pady=10)
        
        self.entry = tk.Entry(input_frame, font=("Arial", 12), bg=self.colors["input_bg"],
                             fg=self.colors["text"], relief=tk.FLAT, insertbackground="white")
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=8)
        self.entry.bind("<Return>", self.send_message_event)
        self.entry.focus()
        
        button_frame = tk.Frame(input_frame, bg=self.colors["bg"])
        button_frame.pack(side=tk.RIGHT)
        
        send_btn = tk.Button(button_frame, text="🚀 Send", command=self.send_message,
                            bg=self.colors["button_bg"], fg=self.colors["text"],
                            font=("Arial", 11, "bold"), relief=tk.FLAT, padx=20)
        send_btn.pack(side=tk.LEFT, padx=5)
        
        emoji_btn = tk.Button(button_frame, text="😊", command=self.insert_emoji,
                             bg=self.colors["button_bg"], fg=self.colors["text"],
                             font=("Arial", 12), relief=tk.FLAT, width=3)
        emoji_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(button_frame, text="🗑️", command=self.clear_chat,
                             bg="#e74c3c", fg=self.colors["text"],
                             font=("Arial", 12), relief=tk.FLAT, width=3)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        suggestion_frame = tk.Frame(self.root, bg=self.colors["bg"])
        suggestion_frame.pack(fill=tk.X, padx=15, pady=(0, 10))
        
        suggestions = ["Say hello 👋", "Tell me a joke 😄", "How are you?", "Goodbye 👋"]
        for suggestion in suggestions:
            btn = tk.Button(suggestion_frame, text=suggestion, command=lambda s=suggestion: self.use_suggestion(s),
                           bg=self.colors["input_bg"], fg=self.colors["text"],
                           font=("Arial", 9), relief=tk.FLAT, padx=10, pady=5)
            btn.pack(side=tk.LEFT, padx=5)
        
        self.welcome_message()
    
    def send_message_event(self, event=None):
        self.send_message()
    
    def welcome_message(self):
        welcome_text = "✨ Welcome to SparkBot! ✨\n\n"
        welcome_text += "I'm your friendly chatbot assistant!\n"
        welcome_text += "Try saying hello, ask for a joke, or use the quick buttons above!\n"
        welcome_text += "Type 'help' if you need suggestions!\n\n"
        self.display_message(welcome_text, "bot")
    
    def display_message(self, message, sender):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender.upper()}: ", sender)
        self.chat_area.insert(tk.END, f"{message}\n\n")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.yview(tk.END)
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        if any(word in user_input for word in ["hello", "hi", "hey"]):
            return random.choice(self.responses["greeting"])
        elif "how are you" in user_input:
            return random.choice(self.responses["howareyou"])
        elif any(word in user_input for word in ["bye", "goodbye", "see you"]):
            self.root.after(1500, self.root.destroy)
            return random.choice(self.responses["bye"])
        elif "name" in user_input:
            return random.choice(self.responses["name"])
        elif "joke" in user_input:
            return random.choice(self.responses["joke"])
        elif any(word in user_input for word in ["love", "like", "hug"]):
            return random.choice(self.responses["love"])
        elif "weather" in user_input:
            return random.choice(self.responses["weather"])
        elif "help" in user_input:
            return random.choice(self.responses["help"])
        else:
            responses = [
                "That's interesting! Tell me more! 🤔",
                "I'm learning from our conversation! 🌱",
                "Could you rephrase that? I want to understand better!",
                "Hmm, that's new to me! Let's talk about something else?",
                f"You said: '{user_input}'. I'm still learning! 😊"
            ]
            return random.choice(responses)
    
    def send_message(self):
        user_input = self.entry.get().strip()
        if user_input:
            self.display_message(user_input, "user")
            
            if user_input.lower() in ["clear", "reset"]:
                self.clear_chat()
                return
            
            self.entry.delete(0, tk.END)
            
            self.root.after(500, lambda: self.respond(user_input))
    
    def respond(self, user_input):
        response = self.get_response(user_input)
        
        typing_indicator = "▌"
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"BOT: {typing_indicator}", "bot")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.yview(tk.END)
        
        for i in range(3):
            self.root.after(200 * i, self.update_typing_indicator, i)
        
        self.root.after(700, self.show_final_response, response)
    
    def update_typing_indicator(self, step):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete("end-2c", "end-1c")
        dots = "." * (step % 3 + 1)
        self.chat_area.insert(tk.END, f"▌{dots}", "bot")
        self.chat_area.configure(state=tk.DISABLED)
        self.chat_area.yview(tk.END)
    
    def show_final_response(self, response):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete("end-2c", "end-1c")
        self.display_message(response, "bot")
        
        if any(word in response.lower() for word in ["goodbye", "bye"]):
            self.root.after(1000, lambda: messagebox.showinfo("Goodbye!", "Thanks for chatting with SparkBot! ❤️"))
    
    def insert_emoji(self):
        emojis = ["😊", "😂", "🤔", "😎", "🥳", "❤️", "🌟", "🎉", "🤖", "🌈"]
        emoji = random.choice(emojis)
        self.entry.insert(tk.END, emoji)
    
    def use_suggestion(self, suggestion):
        self.entry.delete(0, tk.END)
        clean_text = suggestion.replace("👋", "").replace("😄", "").strip()
        self.entry.insert(0, clean_text)
    
    def clear_chat(self):
        self.chat_area.configure(state=tk.NORMAL)
        self.chat_area.delete(1.0, tk.END)
        self.chat_area.configure(state=tk.DISABLED)
        self.welcome_message()

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()