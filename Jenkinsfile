pipeline {
    agent any
    stages {
        stage('Docker build') {
            steps {
                script {
                    try {
                        echo "Building Docker image ..."
                        sh '''
                            docker-compose up --build
                        '''
                    } catch (Exception e) {
                        mail bcc: '', body: 'The Docker build failed.', subject: 'Job Failed', to: 'nickolay.yakovkin@gmail.com'
                    }
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
