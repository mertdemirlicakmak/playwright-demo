pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv $VENV_DIR
                source $VENV_DIR/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                source $VENV_DIR/bin/activate
                pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'results.xml'
        }
    }
}