# Avaliação de Técnicas de Controle de Qualidade no Desenvolvimento de Software Utilizando Metodologias Ágeis

## Equipe

* Davi Augusto Dias Soares
* Victor Lucas Tornelli
* Orientador: Lesandro Ponciano

## Introdução

Com a crescente adoção de metodologias ágeis, o foco na eficiência e entrega contínua de software ganhou destaque. No entanto, a qualidade do software nem sempre recebe a atenção adequada, especialmente em ambientes ágeis que priorizam a funcionalidade sobre a documentação detalhada. Estudos recentes destacam a necessidade de integrar práticas robustas de controle de qualidade no ciclo de desenvolvimento ágil para mitigar falhas e melhorar a eficiência geral.

### Tema
Avaliação de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis.

### Problema
Como as diferentes técnicas de controle de qualidade impactam a eficiência e eficácia do desenvolvimento de software em projetos ágeis?

### Objetivo Geral
Avaliar o impacto de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis, analisando sua eficácia em manter a qualidade e eficiência dos projetos.

### Objetivos Específicos

1. Contrastar diferentes técnicas de controle de qualidade, como testes automatizados, code reviews e integração contínua, no contexto de projetos ágeis.
2. Distinguir o impacto dessas técnicas no ciclo de desenvolvimento de software, medindo fatores como detecção de erros e produtividade das equipes.
3. Analisar se a adoção e eficácia das técnicas de controle de qualidade são influenciadas por características dos projetos, como tamanho da equipe, popularidade e complexidade do software.

## Fundamentação Teórica

A literatura recente em metodologias ágeis sugere que práticas como integração contínua, code review e testes automatizados podem trazer melhorias significativas na qualidade do código P. Karhapää et al., "Evidence-Based Quality-Aware Agile Software Development Process: Design and Evaluation," in IEEE Access, vol. 12, pp. 86487-86512, 2024, doi: 10.1109/ACCESS.2024.3414614. . Contudo, a implementação dessas práticas nem sempre é trivial. Estudos destacam a necessidade de um processo baseado em evidências para garantir que as decisões relacionadas à qualidade sejam bem fundamentadas (Lou et al., 2023).

## Trabalhos Relacionados

1. Karhapää et al. (2024) discutem um processo de desenvolvimento ágil consciente da qualidade, utilizando evidências para tomada de decisão.
2. Beck et al. (2022) exploram os desafios de integrar requisitos de qualidade em métodos ágeis.
3. Smith e Jones (2023) analisam o impacto de diferentes tamanhos de equipe na eficácia das práticas de code review.

## Materiais e Métodos

### Ferramentas e Dados

A pesquisa será do tipo quantitativa, com foco na análise de dados reais extraídos de projetos de software que utilizam metodologias ágeis. Os dados coletados serão analisados utilizando técnicas estatísticas para identificar padrões e correlações entre a aplicação de práticas de controle de qualidade e os resultados obtidos em termos de eficiência e qualidade do software.

* **Projetos Selecionados**: Serão selecionados 9 projetos de diferentes níveis de complexidade no GitHub.
* **Coleta de Dados**: Dados extraídos de commits, pull requests e code reviews via API do GitHub 

### Métricas de Controle de Qualidade

1. **Frequência de comits**: Mede a regularidade das contribuições ao código. Frequências mais altas podem indicar ciclos ágeis curtos e feedback contínuo.
2. **Code Review Time**: Tempo médio para aprovação de código.

### Análise Estatística

* **Correlação de Spearman**: Avaliará a relação entre a adoção das práticas de qualidade e características do projeto, como popularidade e complexidade.

---

Referências

1. **Karhapää, P., et al.** "Evidence-Based Quality-Aware Agile Software Development Process: Design and Evaluation." IEEE Access, 2024. DOI: 10.1109/ACCESS.2024.3414614.
2. **K. Andriadi, H. Soeparno, F. L. Gaol and Y. Arifin**, "The Impact of Shift-Left Testing to Software Quality in Agile Methodology: A Case Study," 2023 International Conference on Information Management and Technology (ICIMTech), Malang, Indonesia, 2023, pp. 259-264, doi: 10.1109/ICIMTech59029.2023.10277919.
3. **Rahman, Mohammad Masudur; Roy, Chanchal K.** "Impact of Continuous Integration on Code Reviews." in *Proceedings of the 2017 IEEE/ACM 14th International Conference on Mining Software Repositories (MSR)*, Buenos Aires, Argentina, 2017, pp. 499-502, doi: 10.1109/MSR.2017.39
4. **Tommy, Robin; Mhaisekar, Meghana; Kallepally, Sangeeta; Varghese, Libin; Ahmed, Shabbir; Somaraju, Madhuri Devi.** "Dynamic Quality Control in Agile Methodology for Improving the Quality," in *2015 IEEE International Conference on Computer Graphics, Vision and Information Security (CGVIS),* Bhubaneswar, India, 2015, pp. 233-236, doi: 10.1109/CGVIS.2015.7449927
