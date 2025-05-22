def get_expected_intent(text: str) -> str:
    text = text.lower().strip()

    intent_keywords = {
        "access_logs": [
            "access log", "audit trail", "usage report", "log history", "view logs", "check logs",
            "session record", "user activity", "login records", "event log"
        ],
        "accessibility_support": [
            "accessibility options", "screen reader", "voice commands", "assistive tech", "vision help",
            "hearing support", "accessible features", "read aloud", "text to speech", "zoom text"
        ],
        "adaptive_learning": [
            "adaptive learning", "personalized lessons", "smart study", "custom learning", "learning style",
            "dynamic course", "learning pattern", "intelligent tutor", "adjust curriculum", "real-time feedback"
        ],
        "add_gp_report": [
            "add gp report", "upload medical file", "submit doctor note", "add health record",
            "add patient report", "include gp file", "record diagnosis", "add medical summary", "submit report"
        ],
        "add_to_grocery_list": [
            "add to shopping list", "add groceries", "put in basket", "grocery item", "add milk",
            "add eggs", "add food", "add snack", "add to cart", "append to list"
        ],
        "affirmative": [
            "yes", "yeah", "sure", "definitely", "of course", "ok", "okay", "affirmative", "sounds good", "correct"
        ],
        "analyze_scene": [
            "analyze view", "what do you see", "describe surroundings", "analyze scene", "object detection",
            "scene detection", "scene analysis", "see the room", "camera scene", "what's in front"
        ],
        "answer_trivia": [
            "answer trivia", "respond to quiz", "solve question", "give answer", "play trivia",
            "trivia response", "answer quiz", "guess answer", "respond to challenge"
        ],
        "ask_bot_name": [
            "what's your name", "who are you", "your name", "bot name", "name please",
            "assistant name", "how do i call you", "tell me your name"
        ],
        "audio_feedback": [
            "make a sound", "audio response", "play tone", "ping", "beep", "sound cue",
            "confirm with audio", "audible feedback", "click sound", "play chime"
        ],
        "audio_playback_control": [
            "pause audio", "resume playback", "play music", "stop sound", "mute", "next song",
            "previous track", "turn off music", "start song", "audio control"
        ],
        "augmented_reality": [
            "start ar", "enable augmented reality", "mixed reality", "launch ar mode",
            "camera overlay", "view in ar", "turn on ar", "augmented experience", "3d overlay", "ar display"
        ],
        "auto_docking": [
            "return to dock", "go charge", "go to station", "autodock", "dock now", "go home",
            "charging base", "docking mode", "self docking", "dock yourself"
        ],
        "autonomous_navigation": [
            "navigate automatically", "go to", "self drive", "robot walk", "auto travel",
            "autonomous mode", "move to room", "pathfinding", "walk on your own", "move there"
        ],
        "battery_alerts": [
            "battery warning", "low battery", "power low", "battery empty", "charge soon",
            "low energy", "battery running out", "battery dying", "battery critical"
        ],
        "battery_status": [
            "battery level", "how much battery", "check power", "battery status",
            "power left", "energy level", "battery percentage", "how much charge", "check battery"
        ],
        "big_data_analysis": [
            "analyze data", "run big data", "big data report", "statistics", "data analysis",
            "predictive model", "train model", "data patterns", "machine learning", "analytics"
        ],
        "bot_feelings": [
            "how do you feel", "bot emotion", "are you happy", "your feelings", "what's your mood",
            "how are you", "robot mood", "bot state", "emotion check", "do you have feelings"
        ],
        "budget_summary": [
            "show budget", "budget overview", "money summary", "monthly spending", "financial report",
            "spending breakdown", "expense summary", "track expenses", "budget chart", "my budget"
        ],
        "calendar_event": [
            "add to calendar", "create event", "schedule task", "add meeting", "set appointment",
            "calendar entry", "event reminder", "create calendar", "calendar note", "add reminder"
        ],
        "calendar_integration": [
            "connect calendar", "link calendar", "sync calendar", "authorize calendar",
            "use google calendar", "add calendar access", "calendar setup", "integrate calendar"
        ],
        "calendar_sync": [
            "resync calendar", "refresh calendar", "update calendar", "sync my events", "calendar update",
            "pull calendar", "synchronize events", "fetch new events"
        ],
                "daily_briefing": [
            "morning summary", "daily overview", "brief me", "daily report", "summary of day",
            "today's plan", "news briefing", "task summary", "schedule overview", "start my day"
        ],
        "daily_summary": [
            "summarize my day", "day overview", "daily wrap", "today summary", "what did i do today",
            "daily insights", "wrap up", "review day", "my activities", "today's progress"
        ],
        "data_logging_consent": [
            "allow data logging", "enable logs", "store data", "consent to logging",
            "record interactions", "data tracking permission", "data collection", "log my activity"
        ],
        "data_security": [
            "secure my data", "protect info", "data safety", "security measures", "privacy settings",
            "encrypt data", "data breach", "security settings", "safe information", "confidential data"
        ],
        "debug_error": [
            "debug mode", "fix error", "troubleshoot", "system issue", "something's wrong",
            "log error", "report bug", "trace issue", "error trace", "problem report"
        ],
        "define_word": [
            "define", "what does it mean", "meaning of", "explain the word", "dictionary",
            "word definition", "vocabulary", "terminology", "lexicon", "what is"
        ],
        "delete_alarm": [
            "delete alarm", "remove alarm", "cancel alarm", "clear alarm", "stop alarm",
            "turn off alarm", "remove wakeup", "disable alarm", "erase alarm"
        ],
        "delete_reminder": [
            "delete reminder", "remove reminder", "cancel reminder", "clear reminder",
            "disable reminder", "forget reminder", "erase task", "cancel task"
        ],
        "describe_surroundings": [
            "what do you see", "describe the area", "what's around", "describe surroundings",
            "see environment", "visual description", "camera view", "what is visible", "look around"
        ],
        "detect_environment": [
            "detect environment", "monitor surroundings", "sense environment", "identify context",
            "check setting", "environment status", "environment scan", "what's the atmosphere",
            "detect air", "sense light"
        ],
        "detect_intrusion": [
            "intruder alert", "detect intruder", "security breach", "motion detection",
            "someone's here", "someone entered", "break in", "alert me if someone comes", "detect movement"
        ],
        "detect_med_chart": [
            "scan medical chart", "analyze med chart", "detect chart", "interpret med data",
            "medical analysis", "check patient record", "chart detection", "extract from chart"
        ],
        "detect_mood": [
            "detect my mood", "how do I feel", "mood detection", "am I happy", "mood analysis",
            "read emotion", "understand my mood", "emotional state", "current mood", "how am I feeling"
        ],
        "detect_motion": [
            "motion detected", "detect movement", "someone moved", "sense motion",
            "movement alert", "is someone there", "detect walking", "movement tracking"
        ],
        "detect_object": [
            "object detection", "see what's there", "what object", "identify thing",
            "camera object", "object scan", "detect items", "spot object", "thing in front"
        ],
        "detect_person": [
            "recognize person", "is someone there", "see person", "identify person",
            "human detected", "who's there", "face detection", "detect human"
        ],
        "detect_pet": [
            "pet detector", "see the dog", "see the cat", "detect pet", "is pet nearby",
            "dog camera", "animal movement", "track pet", "watch pet"
        ],
        "detect_signs_of_life": [
            "any sign of life", "heartbeat detected", "alive", "breathing", "movement",
            "pulse reading", "life detection", "vital sign", "conscious", "signs of movement"
        ],
        "device_connection": [
            "connect to device", "device pairing", "connect phone", "link tablet",
            "device sync", "establish connection", "bluetooth pairing", "connect speaker"
        ],
        "device_integration": [
            "integrate with device", "setup integration", "device link", "external device setup",
            "connect with appliance", "integrate assistant", "new device integration", "sync smart device"
        ],
        "do_not_disturb": [
            "enable do not disturb", "silence mode", "mute notifications", "quiet time",
            "don’t alert", "turn off alerts", "sleep mode", "no interruption", "silent setting"
        ],
        "emergency_alert": [
            "emergency", "sos", "send help", "alert emergency", "panic button", "911",
            "danger", "get help", "urgent", "life threatening"
        ],
        "emergency_protocols": [
            "emergency plan", "what do I do", "safety procedure", "emergency steps",
            "protocol for danger", "safety rules", "respond to emergency", "alert protocol"
        ],
        "empathetic_response_generator": [
            "be empathetic", "kind reply", "understand me", "emotional support", "compassionate response",
            "empathetic chat", "comfort me", "soft response", "be nice"
        ],
        "energy_usage": [
            "energy usage", "power consumption", "electricity report", "used energy",
            "power used", "daily usage", "energy stats", "battery drain", "appliance energy"
        ],
        "entertain_pet": [
            "play with pet", "entertain my dog", "pet activity", "pet time", "keep pet busy",
            "make pet happy", "pet fun", "robot with pet", "pet interaction"
        ],
        "environment_monitoring": [
            "check environment", "monitor air", "air quality", "environment alert",
            "sense pollution", "atmosphere report", "humidity status", "temperature outside"
        ],
        "estimate_arrival": [
            "when will I arrive", "arrival time", "how long to get there", "ETA",
            "estimate travel", "arrival estimate", "time remaining", "when will it reach"
        ],
        "explain_topic": [
            "explain this", "teach me", "what is it", "help me understand", "make it simple",
            "explain the concept", "educate me", "break it down", "give explanation"
        ],
        "face_authentication": [
            "face unlock", "scan my face", "facial login", "face verification", "identify by face",
            "recognize face", "face access", "biometric scan"
        ],
        "fall_detected": [
            "fall alert", "someone fell", "fall detection", "help! someone fell", "accident",
            "falling alert", "emergency fall", "fall sensor triggered"
        ],
        "feed_pets": [
            "feed the dog", "give food to cat", "pet feeding", "automatic feeder", "pet bowl",
            "schedule pet feed", "feed time", "pet breakfast", "dog meal", "cat lunch"
        ],
        "find_place": [
            "where is", "find location", "search for place", "nearest", "closest", "direction to",
            "locate", "place finder", "navigate to", "spot nearby"
        ],
        "fitness_guidance": [
            "guide my workout", "fitness advice", "exercise suggestion", "personal trainer",
            "health tips", "get in shape", "activity plan", "start exercising", "help me train"
        ],
        "fitness_reminder": [
            "remind me to workout", "exercise alert", "fitness nudge", "activity reminder",
            "gym alert", "movement alarm", "time to stretch", "daily workout reminder"
        ],
                "game_launcher": [
            "launch game", "start game", "playstation", "open game", "load game", "video game", "run game",
            "initiate gameplay", "begin match", "arcade mode", "gaming session", "play now"
        ],
        "gesture_interaction": [
            "gesture control", "hand signal", "wave to control", "hand gestures", "motion control",
            "use gesture", "gesture recognition", "gesture navigation", "move by gesture", "hand swipe"
        ],
        "get_device_status": [
            "device status", "status of device", "check speaker", "status report", "get system info",
            "device health", "how’s the device", "device is working", "status check", "is device ok"
        ],
        "get_directions": [
            "how do i get to", "give me directions", "route to", "navigate to", "get there",
            "directions please", "shortest path", "travel directions", "go here", "how to reach"
        ],
        "get_fun_fact": [
            "tell me something fun", "fun fact", "did you know", "surprise me", "give me a fact",
            "cool info", "random fact", "wow me", "entertain me", "fun trivia"
        ],
        "get_nearby_places": [
            "near me", "what's nearby", "nearby restaurants", "places close", "find local spots",
            "local services", "around here", "local info", "any places nearby", "nearby attractions"
        ],
        "get_news": [
            "latest news", "news headlines", "news update", "what's happening", "current affairs",
            "breaking news", "top news", "read the news", "news feed", "today’s headlines"
        ],
        "get_recipe": [
            "how to cook", "recipe for", "make food", "cooking steps", "instructions for meal",
            "cook this", "kitchen help", "show recipe", "prepare meal", "cooking instructions"
        ],
        "get_weather": [
            "what’s the weather", "weather forecast", "check temperature", "weather update", "is it hot",
            "is it raining", "today's weather", "local weather", "temperature outside", "current weather"
        ],
        "goodbye": [
            "bye", "goodbye", "see you later", "talk to you soon", "farewell", "catch you later",
            "see ya", "later", "peace out", "exit", "quit assistant"
        ],
        "greeting": [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening", "yo", "what’s up",
            "greetings", "hiya", "hey assistant"
        ],
        "guided_meditation": [
            "start meditation", "guided meditation", "help me relax", "calm me down", "meditation mode",
            "play calm session", "meditate with me", "breathe in", "breathe out", "relaxation guide"
        ],
        "health_check": [
            "check my health", "health test", "body scan", "run checkup", "diagnose me",
            "how's my health", "health status", "run health check", "analyze vitals"
        ],
        "health_reminder": [
            "remind me to take medicine", "health alarm", "check-up reminder", "drink water",
            "remind for pills", "daily health reminder", "take vitamins", "stay hydrated", "medicine time"
        ],
        "help": [
            "i need help", "how do i", "can you assist", "help me", "show commands", "help options",
            "i’m stuck", "get help", "command list", "what can you do"
        ],
        "help_sleep": [
            "help me sleep", "can't sleep", "play sleep sounds", "soothing music", "sleep better",
            "insomnia", "bedtime music", "calm my mind", "sleepy audio", "sleep mode"
        ],
        "home_status_dashboard": [
            "home status", "how's the house", "house overview", "check home", "status of home",
            "house report", "current home state", "home system", "home dashboard"
        ],
        "household_coordination": [
            "coordinate tasks", "family planner", "shared household", "house duties", "house planning",
            "assign chores", "family schedule", "sync family", "house team tasks", "house checklist"
        ],
        "how_are_you": [
            "how are you", "how do you feel", "how's it going", "are you okay", "how have you been",
            "what’s up with you", "you good", "bot status", "feeling okay"
        ],
        "idle_convo": [
            "let’s chat", "talk to me", "bored", "nothing to do", "start small talk", "idle talk",
            "fun conversation", "free talk", "tell me something", "speak to me"
        ],
        "idle_convo_extended": [
            "keep talking", "longer chat", "tell me more", "go on", "deep talk", "talk more",
            "keep the convo", "extend conversation", "more please", "don't stop"
        ],
        "interactive_storytelling": [
            "tell me a story", "interactive story", "choose adventure", "story mode", "fun story",
            "make a story", "read story", "fictional game", "story play", "adventure mode"
        ],
        "intruder_alerts": [
            "someone’s in the house", "send intruder alert", "trigger alarm", "security alert", "break-in",
            "intruder warning", "unwanted presence", "motion alert", "threat detected", "alert security"
        ],
        "language_practice": [
            "practice language", "learn spanish", "teach me french", "language learning", "how to say",
            "repeat after me", "translate for me", "language lesson", "vocabulary practice", "language exercise"
        ],
        "list_alarms": [
            "show alarms", "list alarms", "my alarms", "check alarms", "scheduled alarms",
            "alarm summary", "what alarms are set", "view alarms", "all alarms"
        ],
        "list_reminders": [
            "show reminders", "list my reminders", "check reminders", "reminder list",
            "upcoming reminders", "scheduled reminders", "reminder summary", "what do i need to do"
        ],
        "lock_doors": [
            "lock the door", "secure the entrance", "lock house", "activate lock", "lock all doors",
            "make sure doors are locked", "secure front door", "close doors", "door lock on"
        ],
        "log_expense": [
            "track spending", "log expense", "add expense", "record payment", "money spent",
            "add cost", "note spending", "log transaction", "save purchase", "financial tracking"
        ],
        "math_help": [
            "solve math", "math question", "calculate", "math help", "what’s 2 plus 2",
            "basic math", "geometry", "arithmetic", "do some math", "algebra question"
        ],
        "media_control": [
            "control media", "pause video", "resume playback", "stop media", "mute audio",
            "play audio", "media commands", "control playback", "video control"
        ],
        "media_playback": [
            "start media", "resume video", "playback on", "continue media", "video playback",
            "watch movie", "resume tv", "stream movie", "play film", "start playback"
        ],
        "media_sharing": [
            "share music", "share video", "send this song", "media share", "send video",
            "send file", "send song", "share content", "stream to friend", "share file"
        ],
        "memory_storage": [
            "save to memory", "remember this", "note this down", "store data", "keep this info",
            "remember my password", "save memory", "record this", "remember that"
        ],
        "mental_checkin": [
            "check how i feel", "mental health", "check my mood", "feeling ok", "mind check",
            "how am i feeling", "emotional check", "mental wellness", "headspace check", "check stress level"
        ],
        "mental_health_checkin": [
            "mental health check", "wellbeing check", "depression check", "am i ok", "emotional scan",
            "stress check", "burnout test", "wellness review", "mental state", "mood survey"
        ],
        "mock_intent": [
            "mock test", "testing intent", "simulate command", "run fake intent", "mockup request",
            "demo mode", "testing only", "debug call", "fake intent", "testing trigger"
        ],
        "monitor_pets": [
            "watch pets", "check on dog", "monitor cat", "pet camera", "track pet",
            "pet status", "is pet okay", "look at pets", "see the animal", "check animal"
        ],
        "mood_detection": [
            "analyze emotion", "detect mood", "check feeling", "what’s my mood", "mood scan",
            "emotion analysis", "detect feelings", "how do I feel", "mood state", "emotion check"
        ],
        "motivational_quote": [
            "motivate me", "give inspiration", "say something uplifting", "quote of the day",
            "daily motivation", "give me a quote", "encourage me", "something positive", "inspire me"
        ],
        "multi_floor_support": [
            "go upstairs", "navigate floors", "multi-floor mode", "change level", "switch floor",
            "floor transition", "level switch", "go to top floor", "travel up", "go down floor"
        ],
                "name_question": [
            "what's your name", "tell me your name", "who are you", "your identity", "what are you called",
            "assistant name", "bot name", "say your name", "introduce yourself"
        ],
        "negative": [
            "no", "nope", "nah", "not really", "never", "absolutely not", "negative", "cancel", "i don’t agree"
        ],
        "nlp_processing": [
            "natural language", "nlp model", "process sentence", "parse text", "language model",
            "text analysis", "semantic understanding", "language processing", "linguistic model"
        ],
        "notifications": [
            "check notifications", "any alerts", "read messages", "show notifications", "notification summary",
            "recent alerts", "push notifications", "update log", "ping history", "message update"
        ],
        "object_location": [
            "where is my", "find object", "track item", "locate thing", "object location",
            "object tracking", "spot this", "where’s my device", "lost item"
        ],
        "open_garage": [
            "open the garage", "garage door", "lift garage", "garage access", "unlock garage",
            "open car space", "garage opener", "garage entry", "open up garage"
        ],
        "ota_updates": [
            "system update", "check for updates", "update now", "over-the-air update", "ota patch",
            "upgrade version", "update system", "install update", "firmware update", "refresh software"
        ],
        "personalization_engine": [
            "personalize", "adapt to me", "customize settings", "my preferences", "tailor experience",
            "user-specific", "adjust to me", "custom behavior", "make it mine", "preference learning"
        ],
        "play_music": [
            "play music", "start song", "play tune", "music please", "start playlist",
            "play audio", "stream song", "play my jam", "put on music", "play beats"
        ],
        "play_trivia": [
            "play trivia", "quiz me", "ask me a question", "start trivia", "let’s do a quiz",
            "trivia challenge", "question game", "knowledge test", "trivia round", "test me"
        ],
        "privacy_mode": [
            "go private", "activate privacy mode", "secure mode", "don't listen", "stop logging",
            "enable incognito", "anonymous mode", "lock my data", "privacy toggle", "do not track"
        ],
        "profile_management": [
            "edit my profile", "change my name", "update details", "manage user profile", "profile settings",
            "my account info", "update user info", "modify profile", "profile management"
        ],
        "quote_of_the_day": [
            "quote of the day", "daily quote", "today’s quote", "motivational quote", "give me wisdom",
            "inspirational words", "quote please", "give me a quote", "famous quote"
        ],
        "read_book": [
            "read me a book", "open ebook", "start reading", "read aloud", "begin book",
            "continue story", "read chapter", "story time", "read fiction", "book session"
        ],
        "read_gp_report": [
            "read my gp report", "analyze health record", "gp summary", "doctor’s report",
            "medical history", "show gp report", "review medical report", "health document"
        ],
        "recognize_face": [
            "who is this", "recognize this person", "scan face", "identify face", "facial recognition",
            "face match", "who’s in front", "detect who", "match person", "face ID"
        ],
        "recommend_movie": [
            "movie suggestion", "what to watch", "suggest a film", "recommend a movie", "pick a movie",
            "top films", "movie ideas", "good movie", "movie tonight"
        ],
        "recommend_music": [
            "music recommendation", "suggest a song", "what should I listen to", "song ideas",
            "top music", "good song", "music for mood", "playlist ideas", "music mood"
        ],
        "record_video": [
            "record this", "start video", "begin recording", "video capture", "take video",
            "shoot video", "record camera", "start filming", "film now", "camera record"
        ],
        "remote_monitoring": [
            "remote monitoring", "watch home", "remote view", "surveillance mode", "check house",
            "camera stream", "monitor from afar", "observe remotely", "watch surroundings"
        ],
        "repeat_last": [
            "say that again", "repeat", "what did you say", "last command", "replay response",
            "repeat previous", "again please", "repeat last answer", "repeat info"
        ],
        "report_issue": [
            "report problem", "found a bug", "issue alert", "something’s wrong", "report error",
            "tell dev", "problem found", "log issue", "notify error", "send feedback"
        ],
        "request_feedback": [
            "give feedback", "rate me", "was this good", "how was that", "feedback please",
            "ask for rating", "survey", "rate this feature", "get feedback", "user opinion"
        ],
        "reset_settings": [
            "reset settings", "factory reset", "start over", "clear preferences", "wipe data",
            "reset everything", "revert settings", "restore defaults", "default settings"
        ],
        "restart_bot": [
            "restart", "reboot bot", "restart assistant", "reset assistant", "reinitialize",
            "start fresh", "reboot system", "reload bot", "begin again"
        ],
        "rl_improvement": [
            "reinforcement learning", "improve by reward", "learn by feedback", "train with reward",
            "rl module", "rl policy", "trial and error", "self improve", "optimize with rl"
        ],
        "room_transition": [
            "go to another room", "move rooms", "change room", "navigate to room", "switch to kitchen",
            "move to hallway", "go to bedroom", "walk to room", "transition room", "next room"
        ],
        "routine_scheduler": [
            "set routine", "schedule daily tasks", "make a schedule", "routine planner", "automate schedule",
            "routine setup", "habit tracker", "daily plan", "create routine"
        ],
                "safe_operation_monitoring": [
            "safe operation", "monitor safety", "watch system health", "hazard check", "risk analysis",
            "safety monitor", "system safe", "detect issues", "operation status", "track safety"
        ],
        "safe_path_planning": [
            "safe route", "calculate path", "plan route", "avoid traffic", "navigate safely",
            "plan safest path", "route optimization", "secure travel", "avoid danger"
        ],
        "schedule_meeting": [
            "schedule meeting", "set appointment", "book a call", "meeting planner", "create event",
            "add meeting", "calendar entry", "plan a call", "schedule session", "set up meeting"
        ],
        "screen_control": [
            "turn off screen", "screen brightness", "dim display", "control screen", "screen power",
            "screen off", "monitor control", "adjust screen", "display settings"
        ],
        "security_system_integration": [
            "connect security system", "integrate with alarm", "security integration", "link security",
            "enable system", "security connection", "alarm system", "security sync", "home defense"
        ],
        "sensor_status": [
            "check sensors", "sensor status", "is sensor working", "sensor health", "motion sensor",
            "temperature sensor", "status of sensor", "sensor report", "sensor reading"
        ],
        "sentiment_report": [
            "emotion summary", "sentiment report", "emotional feedback", "how do I feel",
            "mental state", "daily mood", "emotion tracker", "analyze emotions"
        ],
        "set_alarm": [
            "set alarm", "alarm at", "wake me up", "create alarm", "morning alarm",
            "daily alarm", "alarm for tomorrow", "add alarm", "schedule wakeup"
        ],
        "set_preferences": [
            "set preferences", "update settings", "change config", "adjust options", "user preferences",
            "set defaults", "define my options", "change preferences", "tune settings"
        ],
        "set_recurring": [
            "repeat alarm", "recurring reminder", "weekly task", "repeat every day", "set it daily",
            "repeating schedule", "loop reminder", "schedule weekly"
        ],
        "set_timer": [
            "set timer", "countdown", "start timer", "5 minute timer", "timer for cooking",
            "kitchen timer", "alarm in minutes", "timer set", "begin countdown"
        ],
        "sharing_convo": [
            "share this conversation", "send chat log", "conversation sharing", "share dialogue",
            "send talk", "share our discussion", "export chat", "share chat"
        ],
        "show_home_status": [
            "home summary", "show status", "how's everything", "system check", "status dashboard",
            "overview", "house condition", "device status", "home report"
        ],
        "show_logs": [
            "show logs", "event history", "interaction logs", "past activity", "activity history",
            "log report", "review past", "view logs", "command history"
        ],
        "shutdown_bot": [
            "shutdown", "turn off assistant", "power down", "terminate", "end session",
            "stop bot", "sleep mode", "exit assistant", "bot off"
        ],
        "smart_appliance_management": [
            "manage smart appliances", "control fridge", "control washer", "manage devices",
            "smart kitchen", "smart control", "home automation", "appliance settings", "device tuning"
        ],
        "smart_greetings": [
            "greet smartly", "hello with time", "custom greetings", "good morning assistant",
            "evening greeting", "respond to greeting", "personalized greeting"
        ],
        "smart_kitchen": [
            "kitchen automation", "cook assistant", "smart recipe", "help in kitchen", "automate cooking",
            "cooking machine", "control oven", "kitchen helper", "recipe assistant"
        ],
        "smart_remote_integration": [
            "integrate with remote", "tv remote", "control tv", "smart remote", "remote pairing",
            "remote settings", "remote link", "remote access"
        ],
        "start_game": [
            "start game", "game time", "launch game", "initiate gameplay", "begin match",
            "play now", "gaming mode", "start match", "begin level"
        ],
        "start_routine": [
            "start my routine", "begin schedule", "run morning plan", "initiate workflow",
            "routine on", "execute daily plan", "follow checklist", "routine go"
        ],
        "start_trivia": [
            "start trivia", "begin quiz", "ask trivia", "trivia time", "quiz time",
            "test knowledge", "fun facts game", "trivia now"
        ],
        "start_video_call": [
            "start video call", "video chat", "call with video", "facetime", "begin video session",
            "initiate call", "zoom call", "hangout", "meet now"
        ],
        "start_workout": [
            "start workout", "begin exercise", "train now", "launch fitness", "exercise mode",
            "fitness session", "workout plan", "start gym", "start fitness"
        ],
        "step_by_step_cooking": [
            "step by step recipe", "cooking instructions", "how to cook", "cooking guide",
            "follow recipe", "next cooking step", "walkthrough cooking"
        ],
        "stream_cam": [
            "stream camera", "live camera feed", "video surveillance", "camera on", "see live",
            "live stream", "camera view", "start stream", "cam monitor"
        ],
        "suggest_activity": [
            "suggest activity", "what should I do", "give me a task", "idea for now",
            "recommend something", "fun ideas", "productivity ideas", "activity tip"
        ],
        "suggest_feature": [
            "suggest feature", "feature request", "new idea", "improve assistant",
            "submit suggestion", "ask for feature", "add feature", "propose feature"
        ],
        "summarize_conversation": [
            "summarize our chat", "conversation summary", "what did we talk about",
            "recap conversation", "summarize discussion", "brief of chat", "summary"
        ],
        "surveillance_patrol": [
            "start patrol", "security patrol", "camera check", "scan the house", "go on patrol",
            "move and scan", "watch around", "security round", "active patrol"
        ],
        "take_photo": [
            "take a photo", "snap picture", "capture image", "camera photo", "shoot picture",
            "click photo", "take pic", "take snapshot", "record photo"
        ],
        "task_management": [
            "manage tasks", "add task", "delete task", "update task", "to-do list",
            "assign task", "edit task", "mark task", "task planner"
        ],
        "tell_joke": [
            "tell me a joke", "funny joke", "make me laugh", "joke please", "tell something funny",
            "i need a laugh", "say something funny", "crack a joke"
        ],
        "tell_me_about_you": [
            "who are you", "what can you do", "about yourself", "what are you", "introduce yourself",
            "tell me about chapo", "describe yourself", "your story"
        ],
        "thank_you": [
            "thank you", "thanks", "cheers", "much appreciated", "thanks a lot",
            "thank you very much", "ta", "grateful", "appreciate it"
        ],
        "time_now": [
            "what's the time", "current time", "tell me the time", "time now", "clock check",
            "what time is it", "check time", "time please"
        ],
        "timezone_check": [
            "check timezone", "what timezone", "convert time", "timezone info", "what’s my timezone",
            "time difference", "zone check", "current timezone"
        ],
        "track_medication": [
            "track meds", "medicine schedule", "pill tracker", "when to take medicine",
            "log medication", "check medicine log", "medication reminder"
        ],
        "track_order": [
            "track my order", "where is my package", "order status", "check delivery",
            "shipping status", "track shipping", "where’s my order"
        ],
        "translate_phrase": [
            "translate this", "how do you say", "translate phrase", "language conversion",
            "say it in", "translate to", "what does this mean in"
        ],
        "trivia_question": [
            "ask trivia", "trivia game", "test my knowledge", "question challenge", "quiz me",
            "fun question", "interesting fact", "quiz challenge"
        ],
        "turn_off_lights": [
            "turn off the lights", "switch lights off", "lights out", "kill the lights",
            "disable lighting", "no more lights", "darken room"
        ],
        "turn_on_lights": [
            "turn on the lights", "switch lights on", "light up room", "enable lighting",
            "illuminate", "lights on", "brighten up", "room light on"
        ],
        "turn_on_tv": [
            "turn on tv", "switch on tv", "start television", "tv on", "television start",
            "watch tv", "begin watching", "enable screen"
        ],
        "unlock_doors": [
            "unlock the door", "open the lock", "door open", "unlock house", "door access",
            "disable lock", "open gate", "unsecure entrance"
        ],
        "user_feelings": [
            "i feel", "my mood is", "i’m feeling", "my emotions", "this is how i feel",
            "emotionally", "describe my feeling"
        ],
        "video_call_friend": [
            "video call", "call friend", "facetime friend", "start video chat", "call using video",
            "start facetime", "video call now", "call buddy"
        ],
        "vision_detect_objects": [
            "see object", "detect item", "camera detect", "visual object detection", "identify object",
            "see what's in front", "detect visual"
        ],
        "visual_recognition": [
            "recognize image", "visual scan", "image analysis", "see photo", "photo recognition",
            "analyze picture", "visual understanding"
        ],
        "voice_authentication": [
            "verify my voice", "voice unlock", "voice recognition", "authenticate with voice",
            "access by voice", "secure by voice", "voice login"
        ],
        "voice_command": [
            "voice control", "command with voice", "tell assistant", "speak to bot", "say it aloud",
            "use voice", "talk to assistant", "use command"
        ],
        "voice_command_routing": [
            "route voice command", "delegate request", "pass command", "voice intent routing",
            "transfer voice task", "route what i said", "reroute command"
        ],
        "voice_controls": [
            "use voice controls", "control using voice", "manage with voice", "control devices verbally",
            "talk to control", "voice interactions", "speech control"
        ],
        "wake_word_settings": [
            "change wake word", "set trigger word", "wake word config", "customize wake phrase",
            "update wake word", "set assistant name", "trigger phrase"
        ],
        "water_plants": [
            "water my plants", "plant watering", "garden water", "irrigate", "moisture plants",
            "hydrate plants", "watering schedule", "auto water"
        ],
        "weather_forecast": [
            "forecast for tomorrow", "weekly weather", "future forecast", "what will the weather be",
            "next week’s weather", "next day temperature", "future weather prediction"
        ],
        "web_connectivity": [
            "check internet", "wifi status", "are we online", "internet connection", "web access",
            "online check", "network check", "web status"
        ],
        "what_can_you_do": [
            "what can you do", "features list", "abilities", "help options", "skills overview",
            "show features", "assistant capabilities", "available commands"
        ],
        "wit/get_weather": [
            "weather", "temperature", "forecast", "today’s weather", "how hot", "how cold", "raining", "snowing"
        ]

    }

    for intent, keywords in intent_keywords.items():
        if any(kw in text for kw in keywords):
            return intent

    print(f"🚫 No keyword match for: '{text}'")
    return "unknown"
