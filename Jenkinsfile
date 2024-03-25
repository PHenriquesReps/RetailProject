pipeline {
    agent any       // Jenkins have master and workeer node. "Any" is to not wait for any specific node, run in any node.
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install --user pipenv'
                sh '/jenkins/home/.local/bin/pipenv --rm || exit 0'
                sh '/jenkins/home/.local/bin/pipenv install'
                echo "build completed successfully"
            }
        }
        stage('Test') {
            steps {
                sh '/jenkins/home/.local/bin/pipenv run pytest'
                echo "test completed successfully"
            }
        }
        stage('Package') {
            steps {
                sh 'zip -r retailproject.zip .'
                echo "package completed successfully"
            }
        }
        stage('Deploy') {
            steps {
               echo "deploy completed successfully"
            }
        }
  
    }
}