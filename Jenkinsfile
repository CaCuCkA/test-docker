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
        stage('Run Test with venv') {
            steps {
                script {
                    try {
                        echo "Running tests with venv in Docker container ..."
                        sh '''
                            bash -c "source /home/Mykola/venv/bin/activate &&  python -m unittest discover -s /home/Mykola/test"
                        '''
                    } catch (Exception e) {
                        mail bcc: '', body: 'The test execution failed.', subject: 'Test Failed', to: 'nickolay.yakovkin@gmail.com'
                        error("Stopping pipeline due to failure in test execution.")
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
                echo "Sending POST request to Flask server ..."
                sh '''
                    curl -X POST http://34.118.74.202:5000/success \
                        -H "Content-Type: application/json" \
                        -d '{
                            "status": "completed",
                            "details": "Pipeline execution finished"
                        }'
                '''
            }
        }
        failure {
            script {
                echo "Sending failure notification to Flask server ..."
                sh '''
                    curl -X POST http://34.118.74.202:5000/failure \
                        -H "Content-Type: application/json" \
                        -d '{
                            "status": "failed",
                            "details": "Pipeline execution failed"
                        }'
                '''
            }
        }
    }
}
