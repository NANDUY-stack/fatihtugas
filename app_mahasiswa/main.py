# main.py
from infrastructure.database import Database
from infrastructure.student_repository import StudentRepository
from usecases.student_usecase import StudentUseCase
from presentation.view.student_view import StudentView
from presentation.controllers.student_controller import StudentController
import mysql.connector.plugins.mysql_native_password
import mysql.connector.plugins.caching_sha2_password
def main():
    # 1. Initialize Infrastructure (Database & Repository)
    db = Database(host="localhost", user="root", password="", 
database="db_kampus")
    repo = StudentRepository(db)
    # 2. Initialize Use Case
    usecase = StudentUseCase(repo)
    # 3. Initialize Presentation (View & Controller)
    view = StudentView()
    controller = StudentController(usecase, view)
    # 4. Load Initial Data & Run
    controller.load_students()
    view.mainloop()
if __name__ == "__main__":
    main()