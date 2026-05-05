pipeline {
    agent any

    stages {
        stage('Run CODESYS Simulation') {
            steps {
                bat '"C:\\Program Files\\CODESYS 3.5.16.6\\CODESYS\\Common\\CODESYS.exe" --noUI --runscript="C:\\scripts\\run_simulation.py"'
            }
        }
    }
}
