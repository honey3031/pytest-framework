pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/honey3031/pytest-automation-framework.git'
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

        stage('Clean Docker Containers') {
            steps {
                bat 'docker compose down'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                bat 'docker compose up -d'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest -v'
            }
        }

        stage('Generate Report') {
            steps {
                bat 'venv\\Scripts\\pytest --html=reports/report.html --self-contained-html'
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html'
            bat 'docker compose down'
        }
    }
}