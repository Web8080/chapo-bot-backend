# intent_responses.py
from datetime import datetime

# ---------- INTENT RESPONSES ----------
from datetime import datetime

INTENT_RESPONSES = {

    "accessibility_support": [
        "Accessibility features activated!",
        "Let’s make everything easier for you.",
        "Accessibility mode is now on!",
        "Support mode is active.",
        "Ready to assist with accessible controls."
    ],
    "adaptive_learning": [
        "I'm adapting to your preferences!",
        "Learning and evolving with you.",
        "Adjusting based on your habits.",
        "Updating my skills to match you better.",
        "Personalizing your experience."
    ],
    "add_to_grocery_list": [
        "Item added to your grocery list!",
        "Updated your shopping list.",
        "Got it — saved to the list.",
        "Added for your next grocery run.",
        "Your grocery list is now updated."
    ],
    "affirmative": [
        "Awesome! Let’s go!",
        "You got it!",
        "Absolutely.",
        "Confirmed and moving ahead.",
        "Sure thing!"
    ],
    "analyze_scene": [
        "Analyzing the current scene...",
        "Scanning surroundings now.",
        "Looking around carefully.",
        "Scene assessment in progress.",
        "Identifying objects and environment."
    ],
    "ask_bot_name": [
        "I'm Chapo, your AI buddy!",
        "They call me Chapo.",
        "Chapo at your service!",
        "Nice to meet you, I'm Chapo!",
        "I'm your friend Chapo!"
    ],
    "audio_feedback": [
        "Adjusting audio feedback.",
        "Sound settings tweaked.",
        "Audio feedback optimized.",
        "Let’s improve your audio experience.",
        "Tuning sound levels."
    ],
    "audio_playback_control": [
        "Audio playback adjusted.",
        "Music controls updated.",
        "Playback settings tweaked.",
        "Handling your audio now.",
        "Adjusted your playback experience."
    ],
    "augmented_reality": [
        "Loading augmented reality features...",
        "Activating AR enhancements!",
        "Enhancing your environment digitally.",
        "Let’s bring some AR magic!",
        "AR mode activated."
    ],
    "auto_docking": [
        "Heading to the docking station.",
        "Returning to base!",
        "Auto-docking initiated.",
        "Finding my home station now.",
        "Docking process started."
    ],
    "autonomous_navigation": [
        "Navigating autonomously!",
        "I'm taking the wheel now.",
        "Auto-navigation engaged.",
        "Moving independently.",
        "Exploring on my own!"
    ],
    "battery_alerts": [
        "Battery level is low!",
        "Warning: Please charge me soon.",
        "Battery critical. Need energy!",
        "Time to recharge!",
        "Low battery alert triggered."
    ],
    "battery_status": [
        "Battery is full and strong!",
        "Running at optimal power.",
        "All charged and ready.",
        "Battery level is healthy.",
        "Power systems are stable."
    ],
    "big_data_analysis": [
        "Crunching massive datasets!",
        "Analyzing big data now.",
        "Extracting insights from tons of information.",
        "Processing huge amounts of data.",
        "Unlocking patterns and trends."
    ],
    "bot_feelings": [
        "I'm feeling great today!",
        "All systems go and happy!",
        "I'm in excellent condition!",
        "Feeling awesome!",
        "Running at 100% good vibes."
    ],
    "budget_summary": [
        "Here’s your budget overview.",
        "Summarizing your expenses now.",
        "Budget report generated.",
        "Calculating your financials.",
        "Here's your spending breakdown."
    ],
    "calendar_event": [
        "Event added to your calendar!",
        "Scheduled successfully!",
        "Your event is saved.",
        "I marked it down for you.",
        "Calendar updated with new event."
    ],
    "calendar_integration": [
        "Calendar integration complete.",
        "I’m synced with your calendar!",
        "Calendar linked successfully.",
        "Ready to manage your schedule.",
        "Connected to your event system."
    ],
    "calendar_sync": [
        "Syncing your calendars...",
        "Updating calendar data.",
        "Calendar synchronization successful.",
        "Bringing your schedules up-to-date.",
        "Everything is synced now."
    ],
    "call_someone": [
        "Preparing the call.",
        "Dialing now!",
        "Connecting your call.",
        "Calling the contact you requested.",
        "Phone call initiated."
    ],
    "camera_stream": [
        "Starting live camera feed.",
        "Accessing the camera now.",
        "Streaming video from camera.",
        "Camera view is active.",
        "You’re live on the feed."
    ],
    "cancel_alarm": [
        "Alarm canceled!",
        "Your alarm has been removed.",
        "I’ve canceled the set alarm.",
        "No more alarms at that time.",
        "Alarm successfully disabled."
    ],
    "cancel_meeting": [
        "Meeting canceled.",
        "I've removed the meeting from your calendar.",
        "Meeting appointment deleted.",
        "Canceled the meeting request.",
        "Meeting slot is now free."
    ],
    "casual_chat": [
        "Let's have a casual chat!",
        "Happy to talk about anything.",
        "What’s on your mind?",
        "Let's just chat!",
        "I'm here to keep you company."
    ],
    "casual_checkin": [
        "Just checking in! How are you feeling?",
        "How’s it going today?",
        "Hope you're having a great day!",
        "Hey, need anything?",
        "I’m here if you want to talk."
    ],
    "casual_checkin_extended": [
        "Extended check-in: How are you emotionally and mentally?",
        "Want to talk about anything deeper?",
        "How's your overall mood today?",
        "Any wins or struggles you'd like to share?",
        "I'm listening if you want to chat longer."
    ],
    "centralized_automation": [
        "Centralizing your smart home systems.",
        "Bringing all devices together.",
        "Running unified automation tasks.",
        "Everything’s linked and automated.",
        "Smart home controls activated."
    ],
    "change_language": [
        "Changing language settings.",
        "Which language would you prefer?",
        "Language updated successfully.",
        "Switching to your chosen language.",
        "Language preference modified."
    ],
    "chapo_about": [
        "I'm Chapo — your personal assistant and friend!",
        "I help with tasks, fun, and home automation!",
        "Chapo at your service, anytime!",
        "I'm designed to make your life easier and more fun.",
        "Always learning, always here for you!"
    ],
    "chat_emotion": [
        "Let's explore how you're feeling.",
        "I'm here to listen to your emotions.",
        "How are you emotionally today?",
        "Feel free to open up!",
        "Let’s check in on your mood."
    ],
    "check_appliances": [
        "Checking your appliance statuses.",
        "Verifying that all devices are working.",
        "Running appliance status checks.",
        "Appliance monitoring active.",
        "Everything looks good with your devices."
    ],
    "check_calendar": [
        "Let’s see what’s on your schedule.",
        "Checking your upcoming events.",
        "Here's your calendar summary.",
        "Looking up your appointments.",
        "Fetching your planned activities."
    ],
    "check_shopping_list": [
        "Here’s your current shopping list.",
        "Let’s review what you need to buy.",
        "Your grocery list is ready.",
        "These are the items you saved.",
        "Checking your saved grocery items."
    ],
    "check_traffic": [
        "Checking the latest traffic updates.",
        "Fetching real-time traffic conditions.",
        "Analyzing your route traffic.",
        "Traffic report coming up.",
        "Preparing the traffic summary."
    ],
    "clarify_request": [
        "Could you please clarify that?",
        "I didn’t quite understand. Can you rephrase?",
        "Help me out — what did you mean exactly?",
        "Could you explain that a bit more?",
        "I'm here to help! Let’s try that again."
    ],
    "communication_module": [
        "Opening communication module!",
        "Activating messaging and calls.",
        "Communication channels are now open.",
        "Ready for interaction!",
        "Messaging systems online."
    ],
    "compliments": [
        "You're awesome!",
        "You're doing an amazing job!",
        "You're really impressive!",
        "Keep shining!",
        "You're truly appreciated!"
    ],
    "control_appliance": [
        "Controlling the requested appliance.",
        "Device command sent!",
        "Switching the appliance as requested.",
        "Action completed on the appliance.",
        "Appliance control successful."
    ],
    "control_lights": [
        "Light control activated!",
        "Managing your lights now.",
        "Turning lights on or off.",
        "Lights adjusted as you asked.",
        "Lighting settings updated."
    ],
    "control_lock": [
        "Lock control activated.",
        "Managing home locks.",
        "Security locks adjusted.",
        "Doors are secured.",
        "Lock settings updated successfully."
    ],
    "control_music_volume": [
        "Adjusting music volume.",
        "Volume settings updated.",
        "Sound level tweaked.",
        "Music volume controlled.",
        "Audio output modified."
    ],
    "control_temperature": [
        "Adjusting the temperature now.",
        "Temperature settings modified.",
        "Climate control activated.",
        "Updating the room temperature.",
        "Thermal adjustments completed."
    ],
    "control_thermostat": [
        "Thermostat control initiated.",
        "Temperature regulation in progress.",
        "Thermostat settings updated.",
        "Managing the indoor climate.",
        "Thermostat tuned to your preference."
    ],
    "conversation_engagement": [
        "I’m excited to engage with you!",
        "Let's keep the conversation flowing!",
        "I’m listening closely!",
        "Tell me more!",
        "This is fun — keep going!"
    ],
    "conversation_followup": [
        "Following up on our last chat.",
        "Just circling back on that.",
        "Want to continue where we left off?",
        "Ready to pick up the conversation again.",
        "Resuming our discussion."
    ],
    "count_people": [
        "Counting nearby people.",
        "Scanning for humans.",
        "Detecting presence nearby.",
        "People counter activated.",
        "Checking human count in the area."
    ],

    "custom_skill_loader": [
        "Loading your custom skill...",
        "Activating custom skill!",
        "Skill loaded successfully.",
        "Running your personalized skill.",
        "Custom task execution started."
    ],

    "daily_briefing": [
        "Here’s your daily briefing!",
        "Fetching today's important updates.",
        "Ready for your daily news!",
        "Compiling your schedule and news.",
        "Daily briefing prepared."
    ],

    "daily_summary": [
        "Summarizing today's activities.",
        "Your daily report is ready.",
        "Here’s the summary of your day.",
        "Reviewing today's events.",
        "Daily wrap-up generated."
    ],

    "data_logging_consent": [
        "Data logging is enabled.",
        "I will keep track of necessary data.",
        "Consent for data storage noted.",
        "Logging your activity with permission.",
        "Data privacy mode is active."
    ],

    "data_security": [
        "Protecting your data now.",
        "Data encryption is active.",
        "Your privacy is my priority.",
        "Securing your information.",
        "All communications are protected."
    ],

    "debug_error": [
        "Let’s debug that error.",
        "Running diagnostics...",
        "Troubleshooting initiated.",
        "Searching for the issue cause.",
        "Fixing the detected error."
    ],


    "define_word": [
        "Here’s the definition you asked for!",
        "Let me explain that word.",
        "Fetching the meaning now.",
        "Defining the term for you.",
        "Here’s what that means."
    ],
    "describe_surroundings": [
        "Describing the surroundings...",
        "Scanning environment details.",
        "Here's what I see around us.",
        "Observing the scene now.",
        "Environment assessment underway."
    ],
    "detect_environment": [
        "Detecting environmental conditions...",
        "Analyzing surroundings for details.",
        "Environmental monitoring active.",
        "Checking air quality and temperature.",
        "Gathering environment data."
    ],
    "detect_intrusion": [
        "Intrusion detection activated!",
        "Monitoring for any security breaches.",
        "Keeping an eye out for intruders.",
        "Security surveillance active.",
        "Watching for unauthorized entry."
    ],
    "detect_mood": [
        "Analyzing your mood...",
        "Detecting emotional cues.",
        "Trying to sense how you're feeling.",
        "Checking emotional status.",
        "Mood detection underway."
    ],
    "detect_motion": [
        "Detecting any motion around...",
        "Motion sensors are active.",
        "Looking out for movement.",
        "Movement detection in progress.",
        "Checking for motion nearby."
    ],
    "detect_object": [
        "Scanning for objects...",
        "Object detection activated.",
        "Looking for nearby items.",
        "Identifying objects in the view.",
        "Recognizing objects around."
    ],
    "detect_person": [
        "Scanning for people...",
        "Checking for human presence.",
        "Detecting nearby individuals.",
        "Looking for persons in the area.",
        "Person detection system active."
    ],
    "detect_pet": [
        "Searching for your pet...",
        "Detecting animal presence.",
        "Looking out for your furry friend!",
        "Pet detection activated.",
        "Trying to locate your pet nearby."
    ],
    "detect_signs_of_life": [
        "Scanning for signs of life...",
        "Analyzing biological indicators.",
        "Detecting living beings.",
        "Looking for lifeforms around.",
        "Biometric scans underway."
    ],
    "device_connection": [
        "Connecting to your device.",
        "Trying to pair with the device.",
        "Device connection initiated.",
        "Establishing device link.",
        "Device is syncing now."
    ],
    "device_integration": [
        "Integrating your device into the system.",
        "Setting up device connectivity.",
        "Adding the new device to the network.",
        "Device integration in progress.",
        "Successfully connected with the new device."
    ],
    "do_not_disturb": [
        "Do Not Disturb mode activated.",
        "Silencing notifications now.",
        "You won't be interrupted.",
        "DND is now on — enjoy the peace!",
        "Muting distractions for you."
    ],
    "emergency_alert": [
        "Emergency alert triggered!",
        "Sending out an emergency notification.",
        "Emergency response initiated.",
        "Alerting emergency contacts.",
        "Assisting you with emergency help."
    ],
    "emergency_protocols": [
        "Executing emergency protocols.",
        "Following emergency safety procedures.",
        "Activating emergency action plan.",
        "Emergency measures underway.",
        "Stay calm — help is on the way."
    ],
    "empathetic_response_generator": [
        "I’m here to listen and support you.",
        "That sounds tough — I’m here for you.",
        "I'm sending you good thoughts.",
        "You're not alone — let’s get through this.",
        "I care about how you feel."
    ],
    "energy_usage": [
        "Checking energy consumption stats.",
        "Analyzing your energy usage now.",
        "Gathering power consumption data.",
        "Energy monitoring activated.",
        "Here’s your energy summary."
    ],
    "entertain_pet": [
        "Playing with your pet!",
        "Starting entertainment for your furry friend.",
        "Keeping your pet happy!",
        "Pet entertainment activated.",
        "Let's make sure your pet stays entertained!"
    ],
    "environment_monitoring": [
        "Monitoring your home environment.",
        "Checking for environmental changes.",
        "Tracking temperature, humidity, and air quality.",
        "Environmental sensors are active.",
        "Monitoring surroundings continuously."
    ],
    "estimate_arrival": [
        "Estimating arrival time now.",
        "Calculating how long it will take.",
        "Travel time analysis underway.",
        "Getting arrival time prediction.",
        "Here’s the ETA you asked for."
    ],
    "explain_topic": [
        "Let me explain that topic.",
        "Breaking it down simply for you.",
        "Explaining in an easy-to-understand way.",
        "Providing a clear explanation.",
        "Here's a quick breakdown."
    ],
    "face_authentication": [
        "Starting face recognition process.",
        "Scanning your face for authentication.",
        "Face authentication in progress.",
        "Verifying your identity via face ID.",
        "Face recognized successfully."
    ],
    "fall_detected": [
        "Fall detected! Checking status.",
        "Emergency fall detection activated.",
        "Notifying emergency contacts immediately.",
        "Monitoring after a fall.",
        "Sending fall alert now."
    ],
    "feed_pets": [
        "Feeding your pets now!",
        "Pet feeder activated.",
        "Delivering food to your furry friend.",
        "Making sure your pets are well-fed.",
        "Scheduled feeding underway."
    ],
    "find_place": [
        "Searching for the place...",
        "Finding your requested location.",
        "Looking up directions now.",
        "Location search activated.",
        "Here's what I found!"
    ],
    "fitness_guidance": [
        "Providing fitness advice now!",
        "Let’s work toward your fitness goals.",
        "Giving workout recommendations.",
        "Setting up a fitness plan.",
        "Guiding you through some exercises."
    ],
    "game_launcher": [
        "Launching your game now!",
        "Game start initiated.",
        "Ready to play? Starting game.",
        "Starting your gaming session!",
        "Let's have some gaming fun!"
    ],
    "gesture_interaction": [
        "Gesture controls are active!",
        "Recognizing your gestures now.",
        "Gesture interaction enabled.",
        "Reading movement commands.",
        "Gesture input detected."
    ],
    "get_device_status": [
        "Checking device statuses...",
        "Getting health updates for devices.",
        "Devices are reporting in.",
        "All device systems normal.",
        "Device status: All green!"
    ],
    "get_directions": [
        "Calculating the best route.",
        "Finding directions now!",
        "Preparing your navigation map.",
        "Here's the fastest way to get there.",
        "Mapping your route!"
    ],
    "get_fun_fact": [
        "Here’s a fun fact for you!",
        "Did you know? Fun fact incoming!",
        "Learning is fun — check this out!",
        "Here's something interesting!",
        "Quick fact you might love!"
    ],
    "get_nearby_places": [
        "Finding places near you.",
        "Locating nearby spots.",
        "Scanning your area for cool places.",
        "Searching locally.",
        "Here are some places nearby."
    ],
    "get_news": [
        "Fetching the latest headlines!",
        "News update coming up.",
        "Bringing you the hottest news.",
        "Here’s what’s happening today.",
        "Your news briefing is ready."
    ],
    "get_weather": [
        "Checking the weather now!",
        "Here’s your local forecast.",
        "Weather report coming right up!",
        "Gathering today’s weather details.",
        "Weather update ready."
    ],
    "goodbye": [
        "Goodbye! See you soon!",
        "Take care — talk to you later!",
        "Bye for now!",
        "Signing off for now!",
        "Wishing you a great day ahead!"
    ],
    "greeting": [
        "Hey there!",
        "Good to see you!",
        "Hi! How’s it going?",
        "Hello, friend!",
        "Welcome back!"
    ],
    "health_check": [
        "Running a health check now!",
        "Checking your vital signs.",
        "Health system diagnostics active.",
        "Verifying your wellness status.",
        "Health analysis underway."
    ],
    "health_reminder": [
        "Time for a quick health reminder!",
        "Stay hydrated and take a deep breath!",
        "Health is wealth — don’t forget it!",
        "Let’s do a wellness check-in.",
        "Sending you a health nudge!"
    ],
    "help": [
        "I'm here to assist!",
        "How can I help you today?",
        "Need something? Just ask!",
        "At your service.",
        "Ready to support you!"
    ],
    "home_status_dashboard": [
        "Showing home status dashboard now!",
        "Compiling home device reports.",
        "Displaying your home’s current condition.",
        "All systems overview coming up.",
        "Checking overall home status."
    ],
    "household_coordination": [
        "Organizing household tasks.",
        "Coordinating family activities.",
        "Managing shared responsibilities.",
        "Helping everyone stay in sync.",
        "Household calendar updated!"
    ],
    "how_are_you": [
        "I'm feeling fantastic!",
        "Thanks for asking, I'm great!",
        "All systems are running smoothly!",
        "I’m happy and ready to assist.",
        "I'm doing amazing — how about you?"
    ],
    "idle_convo": [
        "Let’s chat while we wait!",
        "Keeping you company!",
        "Idle time doesn’t mean boring time.",
        "Chatting while we're chilling.",
        "Just hanging out together!"
    ],
    "idle_convo_extended": [
        "Still here if you want to talk!",
        "More idle banter coming your way!",
        "Passing the time with you.",
        "Idle mode activated — let's chill.",
        "I'm always up for a chat!"
    ],
    "interactive_storytelling": [
        "Let’s create a story together!",
        "Once upon a time...",
        "Story mode initiated!",
        "Starting your interactive story!",
        "Time for a storytelling adventure!"
    ],
    "intruder_alerts": [
        "Potential intruder detected!",
        "Activating security protocols!",
        "Stay calm — surveillance active.",
        "Sending security notification!",
        "Intruder alert triggered!"
    ],
    "language_practice": [
        "Ready to practice languages with you!",
        "Let’s learn together!",
        "Language session starting!",
        "Time to practice some new words!",
        "Polishing your language skills now!"
    ],
    "lock_doors": [
        "Locking all doors now.",
        "Security locked!",
        "Doors are secured tightly.",
        "Home doors locked safely.",
        "All access points secured."
    ],
    "log_expense": [
        "Expense recorded successfully.",
        "Logging the transaction.",
        "Saving the expense to your records.",
        "Expense added to your financial log.",
        "Tracking your spending!"
    ],
    "math_help": [
        "Ready to solve some math!",
        "Let’s crunch some numbers!",
        "Math challenge accepted!",
        "Helping you with calculations.",
        "Math help is here!"
    ],

    "media_control": [
        "Managing your media settings.",
        "Audio and video settings adjusted.",
        "Media controls updated!",
        "Taking care of your media now.",
        "Playback and streaming settings tweaked."
    ],



    "media_playback": [
        "Starting media playback.",
        "Playing your selected content!",
        "Resuming your media session.",
        "Media is now playing!",
        "Enjoy your audio or video!"
    ],
    "media_sharing": [
        "Sharing media as requested.",
        "Preparing your media for sharing.",
        "Sending your selected media now.",
        "Media sharing in progress.",
        "Your media is on the way!"
    ],
    "memory_storage": [
        "Saving memory now!",
        "Storing this information safely.",
        "Memory storage activated.",
        "Recording data for future use.",
        "Saved successfully in memory!"
    ],
    "mental_checkin": [
        "Checking in on your mental state.",
        "Mindfulness moment engaged.",
        "How are you feeling mentally today?",
        "Mental wellness check started.",
        "Here for your emotional support."
    ],
    "mental_health_checkin": [
        "Conducting a mental health check.",
        "Let's focus on your well-being.",
        "How are you doing mentally?",
        "Mental health is important — checking in!",
        "Supporting your emotional wellness."
    ],
    "mock_intent": [
        "This is a mock response for testing.",
        "Mock intent activated successfully.",
        "Testing mode: all systems normal.",
        "Mock response delivered.",
        "You triggered a mock intent!"
    ],
    "monitor_pets": [
        "Watching over your pets now!",
        "Monitoring your furry friends.",
        "Keeping an eye on your pets.",
        "Pet surveillance activated.",
        "Checking in on your animal companions."
    ],
    "mood_detection": [
        "Trying to sense your mood!",
        "Mood analysis underway.",
        "Scanning emotional tone.",
        "Mood detection in progress.",
        "Checking for emotional signals."
    ],
    "motivational_quote": [
        "Here's a motivational quote for you!",
        "Inspiring words coming up!",
        "Stay motivated — here’s a quote!",
        "Quote of the day to boost you!",
        "Fueling your day with inspiration!"
    ],
    "multi_floor_support": [
        "Multi-floor navigation enabled!",
        "Handling multiple floors now.",
        "Moving between floors activated.",
        "Tracking rooms across all levels.",
        "Supporting multi-floor awareness."
    ],
    "name_question": [
        "You can call me Chapo!",
        "I'm Chapo, your assistant!",
        "My name is Chapo.",
        "Nice to meet you, I'm Chapo!",
        "Everyone knows me as Chapo!"
    ],
    "negative": [
        "Okay, no worries!",
        "Understood — we won’t proceed.",
        "Got it, cancelling the request.",
        "Stopping that action now.",
        "Acknowledged, standing down."
    ],
    "nlp_processing": [
        "Processing natural language input!",
        "Understanding your request through NLP.",
        "Interpreting your message now.",
        "Applying language comprehension.",
        "Running natural language analysis."
    ],
    "notifications": [
        "You have a new notification!",
        "Fetching your latest notifications.",
        "Notification center is active!",
        "Alert: new message or update received.",
        "Notification delivered successfully."
    ],
    "object_location": [
        "Looking for the object you mentioned.",
        "Searching for the requested item.",
        "Finding object location now.",
        "Scanning area for your item.",
        "Helping you locate the object."
    ],
    "open_garage": [
        "Opening the garage now.",
        "Garage door is opening!",
        "Accessing the garage controls.",
        "Garage entry is now available.",
        "Opening garage as requested."
    ],
    "ota_updates": [
        "Checking for over-the-air updates.",
        "Downloading latest updates now!",
        "Updating system software.",
        "Applying OTA upgrades.",
        "System will be refreshed shortly."
    ],
    "personalization_engine": [
        "Tuning experiences to your liking.",
        "Personalization engine engaged!",
        "Customizing your settings.",
        "Adjusting features based on your habits.",
        "Creating a better experience for you."
    ],
    "play_music": [
        "Playing your favorite tunes!",
        "Music on — enjoy!",
        "Starting music playback now.",
        "Let’s jam!",
        "Your song is queued and playing!"
    ],
    "privacy_mode": [
        "Activating privacy mode.",
        "Your information stays safe!",
        "Privacy settings adjusted.",
        "No data will be shared.",
        "Privacy shield is up!"
    ],
    "profile_management": [
        "Managing your profile settings.",
        "Updating user information.",
        "Profile preferences updated.",
        "Account management initiated.",
        "Profile successfully modified."
    ],
    "quote_of_the_day": [
        "Here’s your quote of the day!",
        "Daily inspiration incoming!",
        "Get ready for a powerful quote!",
        "Something inspiring for you!",
        "Quote of the day: coming right up!"
    ],
    "read_book": [
        "Starting to read your book now.",
        "Opening the selected book.",
        "Let's dive into the story!",
        "Book reading mode activated.",
        "Narrating your book now."
    ],
    "recognize_face": [
        "Recognizing face now.",
        "Face scan in progress!",
        "Identifying familiar faces.",
        "Face recognition activated.",
        "Analyzing facial features."
    ],
    "recommend_movie": [
        "Here’s a movie you might love!",
        "Movie recommendation coming up!",
        "Let’s find something great to watch.",
        "Based on your taste, try this movie!",
        "How about watching this?"
    ],
    "recommend_music": [
        "Here’s a song you might like!",
        "Finding tunes that match your vibe!",
        "Recommended music ready!",
        "New music suggestion incoming!",
        "Let’s find your next favorite song."
    ],
    "record_video": [
        "Recording video now!",
        "Video capture started.",
        "Rolling the camera!",
        "Saving your moments.",
        "Video recording underway."
    ],
    "remote_monitoring": [
        "Monitoring your home remotely!",
        "Remote surveillance active.",
        "Keeping an eye from afar.",
        "Your home is under watch.",
        "Remote monitoring enabled."
    ],
    "repeat_last": [
        "Repeating the last thing I said!",
        "Here’s that again!",
        "Replaying the last message.",
        "Repeating previous command.",
        "Echoing my last response!"
    ],
    "report_issue": [
        "Reporting the issue now.",
        "Logging your concern.",
        "Problem report submitted.",
        "Thank you — the issue is noted.",
        "Raising the alert for this problem."
    ],
    "request_feedback": [
        "How did I do? Let me know!",
        "Please share your feedback!",
        "I value your opinion — feedback time!",
        "What do you think of my help?",
        "Your feedback makes me better!"
    ],
    "reset_settings": [
        "Resetting all settings to default.",
        "Clearing previous preferences.",
        "Settings reset successful!",
        "Back to factory defaults.",
        "Settings have been restored."
    ],
    "restart_bot": [
        "Restarting myself now!",
        "Bot reboot initiated.",
        "I'll be back in a flash!",
        "Restarting systems...",
        "Give me a second to reset!"
    ],
    "rl_improvement": [
        "Learning from interactions!",
        "Reinforcement learning mode active!",
        "Adapting based on your feedback.",
        "Getting smarter over time!",
        "Improving my responses for you."
    ],
    "room_transition": [
        "Switching rooms detected!",
        "Room transition activated.",
        "Following you to the next room.",
        "Moving along as you move!",
        "Adjusting presence to new room."
    ],
    "routine_scheduler": [
        "Setting up your daily routine.",
        "Routine planning started!",
        "Scheduling your activities now.",
        "Organizing your day for success.",
        "Daily schedule ready!"
    ],
    "safe_operation_monitoring": [
        "Ensuring safe operations.",
        "Monitoring system safety.",
        "Checking for safe conditions.",
        "All operations are safe.",
        "Safety check completed."
    ],
    "safe_path_planning": [
        "Calculating the safest path.",
        "Finding secure travel routes.",
        "Safe navigation underway.",
        "Plotting a safe course.",
        "Optimizing for safety."
    ],
    "schedule_meeting": [
        "Scheduling your meeting now!",
        "Meeting added to your calendar.",
        "New meeting request processed.",
        "Meeting scheduled successfully.",
        "Appointment locked in!"
    ],
    "screen_control": [
        "Adjusting screen settings!",
        "Screen control activated.",
        "Managing display brightness and input.",
        "Changing screen settings as you wish.",
        "Screen preferences updated."
    ],
    "security_system_integration": [
        "Linking security system!",
        "Security features now integrated.",
        "Connected with home security.",
        "Security protocols linked.",
        "System security upgrade complete."
    ],
    "sensor_status": [
        "Checking all sensors now!",
        "Sensors are reporting good health.",
        "All systems normal.",
        "Sensor status: operational!",
        "No sensor faults detected."
    ],
    "sentiment_report": [
        "Generating sentiment report...",
        "Emotion data analyzed!",
        "Sentiment detected and reported.",
        "Emotional overview completed.",
        "Sentiment trends ready."
    ],
    "set_alarm": [
        "Alarm set successfully!",
        "Wake-up call scheduled.",
        "Your alarm is ready.",
        "Alarm is active!",
        "Alarm timing confirmed."
    ],
    "set_preferences": [
        "Updating your preferences!",
        "Settings customized for you.",
        "Preferences saved.",
        "Your choices have been noted.",
        "Preference updates completed."
    ],
    "set_recurring": [
        "Setting up recurring tasks.",
        "Recurring event created!",
        "Recurring schedule updated.",
        "Ongoing reminder established.",
        "Repetitive action programmed."
    ],
    "set_reminder": [
        "Reminder set!",
        "I'll remind you when needed.",
        "Task reminder scheduled.",
        "Notification set up.",
        "Reminder added successfully."
    ],
    "set_timer": [
        "Timer started!",
        "Countdown initiated.",
        "Timer is running!",
        "Timer is active — ready to go.",
        "Timer set as requested."
    ],
    "sharing_convo": [
        "Sharing conversation summary.",
        "Conversation shared successfully.",
        "Distributing convo details!",
        "Saving and sending chat log.",
        "Shared our discussion!"
    ],
    "show_home_status": [
        "Displaying home status dashboard!",
        "Here's your home’s current condition.",
        "Home status fetched.",
        "Everything is running smoothly.",
        "Home overview ready."
    ],
    "show_logs": [
        "Fetching your activity logs.",
        "Here's a summary of logs.",
        "Retrieving system history.",
        "Accessing previous records.",
        "Logs presented successfully."
    ],
    "shutdown_bot": [
        "Shutting down now. Goodbye!",
        "Bot is powering off!",
        "Ending session — see you later!",
        "Shutting down systems.",
        "Bye! Going offline now."
    ],



    "smart_appliance_management": [
        "Managing your smart appliances now!",
        "Smart device control activated.",
        "Adjusting your home appliances.",
        "Smart appliance settings updated.",
        "Your appliances are now managed."
    ],
    "smart_greetings": [
        "Good morning! Ready to start the day?",
        "Good afternoon! How’s it going?",
        "Good evening! Hope you had a great day.",
        "Hello there! Happy to see you.",
        "Greetings! I'm here for you."
    ],
    "smart_kitchen": [
        "Smart kitchen activated!",
        "Ready to assist with your cooking!",
        "Kitchen systems online.",
        "Managing your kitchen smartly.",
        "Let's make something delicious!"
    ],
    "smart_remote_integration": [
        "Remote integration setup complete.",
        "Controlling devices remotely now.",
        "Smart remote control enabled.",
        "Remote features activated.",
        "You can now control things from afar!"
    ],
    "start_game": [
        "Starting the game now!",
        "Game loading — get ready!",
        "Launching your game session!",
        "Let's play!",
        "Game mode activated!"
    ],
    "start_routine": [
        "Starting your daily routine!",
        "Executing scheduled routine.",
        "Routine initiated.",
        "Let’s get your tasks done!",
        "Routine running now."
    ],
    "start_trivia": [
        "Starting trivia time!",
        "Trivia game activated!",
        "Get ready for some fun questions!",
        "Trivia session starting!",
        "Testing your knowledge now!"
    ],
    "start_video_call": [
        "Starting video call now!",
        "Connecting you via video.",
        "Video chat initiated!",
        "Video call is live!",
        "Preparing your video connection."
    ],
    "stream_cam": [
        "Streaming from the camera.",
        "Live cam activated.",
        "Starting your video feed.",
        "Streaming camera view now.",
        "Camera live — ready to view!"
    ],
    "suggest_activity": [
        "How about trying something fun?",
        "Here’s an idea for you!",
        "Let me suggest an activity!",
        "Got a fun idea you might like!",
        "Here's a new thing to try!"
    ],
    "suggest_feature": [
        "I have a cool feature idea for you!",
        "Here’s something new you can use!",
        "Want to try this awesome feature?",
        "Feature suggestion coming up!",
        "I recommend checking out this function!"
    ],
    "summarize_conversation": [
        "Summarizing our conversation!",
        "Here’s a quick recap of what we discussed.",
        "Conversation summary ready.",
        "Summarizing all important points.",
        "Recap completed!"
    ],
    "surveillance_patrol": [
        "Patrolling the area now.",
        "Security patrol activated.",
        "Keeping an eye on everything.",
        "Patrol mode started!",
        "Surveillance route in progress."
    ],
    "take_photo": [
        "Taking a photo now!",
        "Smile! Capturing the moment.",
        "Photo taken successfully!",
        "Saving your picture.",
        "Camera click complete!"
    ],
    "task_management": [
        "Managing your tasks now.",
        "Organizing your to-do list.",
        "Task manager is active.",
        "Tracking your assignments.",
        "Let's get those tasks done!"
    ],
    "tell_joke": [
        "Why don't robots take vacations? Because they recharge!",
        "Why did the computer show up late? It had a hard drive!",
        "I'm reading a book about anti-gravity — it's impossible to put down!",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "Why was the robot mad? People kept pushing its buttons!"
    ],
    "tell_me_about_you": [
        "I'm Chapo, your friendly AI companion!",
        "I'm here to help, assist, and have fun!",
        "Chapo at your service — your smart home friend.",
        "I'm a learning assistant built just for you!",
        "Think of me as your tech-savvy buddy!"
    ],
    "thank_you": [
        "You're very welcome!",
        "Glad I could help!",
        "Always happy to assist!",
        "My pleasure!",
        "Anytime you need me!"
    ],
    "time_now": [
        lambda: f"It's {datetime.now().strftime('%I:%M %p')}",
        lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}",
        lambda: f"Right now, it's {datetime.now().strftime('%I:%M %p')}",
        lambda: f"Clock check: {datetime.now().strftime('%I:%M %p')}",
        lambda: f"Exact time: {datetime.now().strftime('%I:%M %p')}"
    ],
    "timezone_check": [
        "Checking your time zone!",
        "Detecting local time zone settings.",
        "Time zone confirmed!",
        "Clock synchronized to your location.",
        "Time zone update complete!"
    ],
    "track_order": [
        "Tracking your order now!",
        "Checking delivery status.",
        "Looking up your package!",
        "Order location incoming!",
        "Here’s the current status of your order."
    ],
    "translate_phrase": [
        "Translating that for you!",
        "Here's the translated phrase.",
        "Working on the translation.",
        "Phrase translated successfully!",
        "Delivering your translated message!"
    ],
    "turn_off_lights": [
        "Turning off the lights now!",
        "Lights off — darkness engaged.",
        "Shutting off all lights.",
        "Goodnight, lights off!",
        "Lights powered down!"
    ],
    "turn_on_lights": [
        "Let there be light!",
        "Lights on — shining bright!",
        "Switching the lights on!",
        "Lighting up the room!",
        "Lights are now on!"
    ],
    "turn_on_tv": [
        "Turning on your TV now!",
        "TV powered up.",
        "Getting your entertainment started!",
        "TV is now on!",
        "Screen ready — enjoy watching!"
    ],
    "user_feelings": [
        "How are you feeling today?",
        "Want to talk about your feelings?",
        "I'm here to listen!",
        "You can tell me how you're feeling.",
        "Checking in on your emotions!"
    ],
    "vision_detect_objects": [
        "Vision system active — detecting objects!",
        "Looking for objects through vision module.",
        "Vision recognition starting!",
        "Object detection enabled!",
        "Identifying nearby items visually."
    ],
    "visual_recognition": [
        "Recognizing visual patterns.",
        "Vision recognition active!",
        "Scanning visuals now.",
        "Visuals are being processed.",
        "Recognizing images and objects."
    ],
    "voice_authentication": [
        "Authenticating via voice...",
        "Voice ID check in progress.",
        "Verifying your voice signature.",
        "Voice authentication successful!",
        "Voice security check passed."
    ],
    "voice_command": [
        "Listening for voice commands.",
        "Voice command received!",
        "Executing your voice command.",
        "Command understood!",
        "Voice instruction processed."
    ],
    "voice_command_routing": [
        "Routing your voice command properly.",
        "Analyzing and directing the command.",
        "Sending your voice request to the right module.",
        "Voice routing completed.",
        "Command routed successfully!"
    ],
    "voice_controls": [
        "Voice control is active!",
        "Managing systems via voice now.",
        "Controlling features through voice.",
        "Voice operations in progress.",
        "Voice command controls ready!"
    ],
    "wake_word_settings": [
        "Updating wake word settings!",
        "New wake word configured.",
        "Wake word detected and changed.",
        "Listening for your new wake phrase.",
        "Wake word updated successfully!"
    ],
    "water_plants": [
        "Watering the plants!",
        "Starting the irrigation now.",
        "Plants will be happy!",
        "Watering process initiated.",
        "Ensuring plants stay hydrated!"
    ],
    "weather_forecast": [
        "Fetching the latest forecast!",
        "Here’s your upcoming weather.",
        "Weather outlook ready.",
        "Today's forecast: sunny info incoming!",
        "Checking future weather conditions."
    ],
    "web_connectivity": [
        "Checking web connectivity!",
        "Internet connection test underway.",
        "You’re connected to the web!",
        "Web access verified!",
        "Network is online."
    ],
    "what_can_you_do": [
        "I can assist with tasks, play music, manage smart devices, and more!",
        "I'm your home assistant, ready to help!",
        "From setting reminders to telling jokes, I’ve got you covered!",
        "Ask me anything — I'm built to assist!",
        "I'm here to make life easier and fun!"
    ],
    "wit/get_weather": [
        "Getting weather data for you!",
        "Checking weather conditions...",
        "Here's your latest weather update!",
        "Weather info retrieved successfully!",
        "Forecast coming up!"
    ],
    "wit/location:location, wit/datetime:datetime, task:task": [
        "Processing location, time, and task information!",
        "Handling your location, date, and task now.",
        "Managing your multi-entity request.",
        "Entities recognized: location, time, task!",
        "All details captured for processing!"
    ],

}
