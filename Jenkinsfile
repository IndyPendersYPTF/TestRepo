
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
        bat 'C:\\Users\\TA\\AppData\\Local\\Programs\\Python\\Python312\\python.exe Test.py'
      }
    }
    
  }
}
