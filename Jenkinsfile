pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-key', url: 'git@github.com:payammirzaei/vehicle_recommendation.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t vehicle-recommendation .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm vehicle-recommendation'
            }
        }
    }

    post {
        success {
            echo '✅ Build and Test Successful!'
        }
        failure {
            echo '❌ Build or Tests Failed!'
        }
    }
}
