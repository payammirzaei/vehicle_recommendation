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

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm vehicle-recommendation'
            }
        }
    }

    post {
        success {
            echo 'Docker Container Built and Ran Successfully! ✅'
        }
        failure {
            echo 'Build or execution failed. ❌'
        }
    }
}
