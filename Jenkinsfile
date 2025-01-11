node {
    // Define variables
    def repoUrl = 'git@github.com:CaCuCkA/test-docker.git'
    def branch = 'main'
    def dockerImage = 'mysql-test-project:latest'

    try {
        // Checkout Code Stage
        stage('Checkout Code') {
            echo 'Fetching data from Git repository...'
            checkout scm
        }

        // Build Docker Image Stage
        stage('Build Docker Image') {
            echo "Building Docker image: ${dockerImage}"
            sh "docker build -t ${dockerImage} ."
        }

        // Notification for Success
        stage('Notification') {
            echo 'Pipeline completed successfully. Sending notification...'
            emailext(
                subject: "Pipeline SUCCESS: ${env.JOB_NAME}",
                body: """
Hello Team,

The Jenkins pipeline for the job [${env.JOB_NAME}] has completed successfully.

**Details:**
- Job Name: ${env.JOB_NAME}
- Build Number: ${env.BUILD_NUMBER}
- Branch: ${branch}
- Build URL: ${env.BUILD_URL}

Best regards,  
Jenkins
                """,
                to: 'nickolay.yakovkin@gmail.com'
            )
        }
    } catch (e) {
        // Notification for Failure
        echo "Pipeline failed: ${e.message}"
        emailext(
            subject: "Pipeline FAILURE: ${env.JOB_NAME}",
            body: """
Hello Team,

The Jenkins pipeline for the job [${env.JOB_NAME}] has failed.

**Details:**
- Job Name: ${env.JOB_NAME}
- Build Number: ${env.BUILD_NUMBER}
- Branch: ${branch}
- Build URL: ${env.BUILD_URL}

**Error Message:**
${e.message}

Please review the logs and take the necessary action.

Best regards,  
Jenkins
                """,
                to: 'nickolay.yakovkin@gmail.com'
            )
        throw e
    }
}
