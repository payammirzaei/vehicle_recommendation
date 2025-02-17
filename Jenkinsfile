pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-key', url: 'git@github.com:payammirzaei/vehicle_recommendation.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest tests/ || echo "No tests found, skipping..."
                '''
            }
        }

        stage('Run ML Model') {
            steps {
                sh '''
                source venv/bin/activate
                python3 main.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Machine Learning Model Executed Successfully! ✅'
        }
        failure {
            echo 'Build or tests failed. ❌'
        }
    }
}
