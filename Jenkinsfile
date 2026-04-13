
pipeline {
  agent any
  stages {
    stage('Print') {
      steps {
        echo 'this works'
      }
    }
    stage('TEST') {
      steps {
        bat 'C:\\Users\\TA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe Twincat_Simulation_pc\\Jenkins\\Test.py'
      }
    }
    
  }
}
