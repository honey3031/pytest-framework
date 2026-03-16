pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/honey3031/pytest-framework.git'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'py -3 -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest'
            }
        }

        stage('Stop Containers') {
            steps {
                bat 'docker compose down'
            }
        }
    }
}