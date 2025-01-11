pipeline {
    agent any
    stages {
        stage('Docker build') {
            steps {
                script {
                    try {
                        echo "Building Docker image ..."
                        sh '''
                            docker-compose up --build -d
                        '''
                    } catch (Exception e) {
                        mail bcc: '', body: 'The Docker build failed.', subject: 'Job Failed', to: 'nickolay.yakovkin@gmail.com'
                        error("Stopping pipeline due to failure in Docker build.")
                    }
                }
            }
        }
        stage('Send Success') {
            steps {
                mail bcc: '', body: 'The pipeline completed successfully!', subject: 'Pipeline Success Notification', to: 'nickolay.yakovkin@gmail.com'
            }
        }
    }
    post {
        always {
            script {
                echo "Stopping Docker containers ..."
                sh '''
                    docker-compose down
                '''
            }
        }
    }
}
