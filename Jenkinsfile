pipeline {
    agent {
        label 'linux_000143'
    }
    
    options {
        timestamps()
        disableConcurrentBuilds()
    }
    stages {
    stage('SCM Checkout') {
    steps {
        cleanWs() // Clean workspace before checking out the code
        checkout([$class: 'GitSCM', branches: [
            [name: 'main'],
            [name: 'branch1']
        ], userRemoteConfigs: [[credentialsId: 'jenkins', url: 'https://github.com/desainiravp/Demo.git']]])
    }
}
stage('Build') {
   
    steps {
        script {
            echo "Building on branch: ${env.BRANCH_NAME}"
            echo 'Building the code...'
            // Add your actual build steps here
        }
    }
}
        }
}
