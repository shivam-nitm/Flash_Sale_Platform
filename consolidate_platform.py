import os
import subprocess
import shutil

BASE_DIR = "/Users/shivam/Desktop/Projects/SelfMadeProjects/SD/Flash_Sale_Platform"

def run_cmd(cmd, cwd=None):
    res = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error executing '{cmd}' in {cwd}: {res.stderr}")
    else:
        print(f"Success: {cmd}")
    return res

sub_dirs = ["catalog-service", "inventory-service", "order-service", "payment-fulfillment-service", "event-bus", "infra-observability", "testing-chaos-lab", "ai-ops-assistant"]

# 1. Remove nested .git directories so they become standard tracked subdirectories in the parent repo
for sub in sub_dirs:
    git_dir = os.path.join(BASE_DIR, sub, ".git")
    if os.path.exists(git_dir):
        print(f"Removing nested .git from {sub}...")
        shutil.rmtree(git_dir)

# 2. Create parent root pom.xml to bind all microservices functionally into a single parent project
parent_pom = """<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.flashsale</groupId>
    <artifactId>flash-sale-platform-parent</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>pom</packaging>
    <name>Flash Sale Platform — Parent Multi-Module Project</name>
    <description>Parent Orchestrator for all Flash Sale Microservices</description>

    <modules>
        <module>catalog-service</module>
        <module>inventory-service</module>
        <module>order-service</module>
        <module>payment-fulfillment-service</module>
        <module>event-bus</module>
        <module>ai-ops-assistant</module>
    </modules>

    <properties>
        <java.version>21</java.version>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <spring-boot.version>3.2.3</spring-boot.version>
    </properties>

    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-dependencies</artifactId>
                <version>${spring-boot.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
</project>
"""

with open(os.path.join(BASE_DIR, "pom.xml"), "w") as f:
    f.write(parent_pom)

# 3. Clean root .gitignore so submodules/dirs are tracked
gitignore_content = """target/
*.log
.idea/
*.class
.DS_Store
*.jar
"""
with open(os.path.join(BASE_DIR, ".gitignore"), "w") as f:
    f.write(gitignore_content)

# 4. Git add all microservice files and commit to main in root parent repo
run_cmd("git add .", cwd=BASE_DIR)
run_cmd("git commit -m 'feat: consolidate all microservices into parent project repository'", cwd=BASE_DIR)

# 5. Push updated main branch to GitHub
run_cmd("git push --force -u origin main", cwd=BASE_DIR)

# 6. Create and push individual microservice branches from the parent repo for developer squads
for sub in sub_dirs:
    print(f"Updating branch {sub} in parent repo...")
    run_cmd(f"git branch -D {sub} 2>/dev/null || true", cwd=BASE_DIR)
    run_cmd(f"git checkout -b {sub}", cwd=BASE_DIR)
    run_cmd(f"git push --force -u origin {sub}", cwd=BASE_DIR)

# Switch back to main branch
run_cmd("git checkout main", cwd=BASE_DIR)
print("Consolidation complete!")
