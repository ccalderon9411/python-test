from sonarqube import SonarQubeClient

sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", token="sqp_bcd4901b9d7bc3f2ee99081eda701acbe6702de1")
project_key = "python-test"

analysis_results = sonar.project_analyses.search_analyses(project=project_key)
for analysis in analysis_results:
    print(analysis)