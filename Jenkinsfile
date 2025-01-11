pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                mail bcc: '', body: 'Test', subject: 'Test', to: 'nickolay.yakovkin@gmail.com'
            }
        }
    }
}