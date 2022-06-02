class Firebase:
    def __init__(self):
        import pyrebase

        firebaseConfig = {
            "apiKey": "AIzaSyCQ33S42z6fXYHUN42V8FBVYrlxzY45m7M",
            "authDomain": "minesweeper-81875.firebaseapp.com",
            "databaseURL": "https://minesweeper-81875-default-rtdb.asia-southeast1.firebasedatabase.app",
            "projectId": "minesweeper-81875",
            "storageBucket": "minesweeper-81875.appspot.com",
            "messagingSenderId": "382802460948",
            "appId": "1:382802460948:web:790408cbba60ccd9c18201"
        }

        firebase = pyrebase.initialize_app(firebaseConfig)

        self.db = firebase.database()
        self.auth = firebase.auth()
        self.storage = firebase.storage()


fire = Firebase()

fire.storage.child('Assets/stage-0.png').put('stage-1.png')
