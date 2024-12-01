# Avaliação de Técnicas de Controle de Qualidade no Desenvolvimento de Software Utilizando Metodologias Ágeis

## Equipe

1. Davi Augusto Dias Soares  
2. Victor Lucas Tornelli  

* **Orientador de Conteúdo:** Lesandro Ponciano  

---

## Introdução  

1. **A área da Engenharia de Software tratada neste trabalho é:** _Avaliação de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis._  
2. **O problema que este trabalho busca resolver nessa área é:** _Como as diferentes técnicas de controle de qualidade impactam a eficiência e eficácia do desenvolvimento de software em projetos ágeis?_  
3. **Resolver este problema é relevante por que:** A crescente adoção de metodologias ágeis nas equipes de desenvolvimento de software tem destacado a necessidade de integrar práticas robustas de controle de qualidade. Essas práticas não só asseguram a manutenção da qualidade do produto, mas também contribuem para a mitigação de falhas e melhoram a eficiência das equipes, reduzindo custos e o tempo de entrega de funcionalidades. A compreensão do impacto de técnicas específicas de controle de qualidade é fundamental para melhorar continuamente esses processos, especialmente em ambientes de desenvolvimento ágeis, que são cada vez mais prevalentes no setor de software (Karhapää et al., 2024).  
4. **O objetivo geral deste trabalho é:** _Avaliar o impacto de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis, analisando sua eficácia em manter a qualidade e eficiência dos projetos._  
5. **Os três objetivos específicos deste trabalho são:**  
   - Contrastar diferentes técnicas de controle de qualidade, como testes automatizados, code reviews e integração contínua, no contexto de projetos ágeis.  
   - Distinguir o impacto dessas técnicas no ciclo de desenvolvimento de software, medindo fatores como detecção de erros e produtividade das equipes.  
   - Analisar se a adoção e eficácia das técnicas de controle de qualidade são influenciadas por características dos projetos, como tamanho da equipe, popularidade e complexidade do software.

---


## Fundamentação Teórica

1. **Conceito principal:** _Metodologias Ágeis._  
   - Definição: "Conjunto de práticas iterativas e incrementais que priorizam entregas rápidas de software funcional por meio de ciclos curtos de desenvolvimento, com ênfase em feedback constante e adaptação às mudanças" (Karhapää et al., 2024, https://doi.org/10.1109/ACCESS.2024.3414614).  

2. **Conceito secundário:** _Integração Contínua._  
   - Definição: "Prática de desenvolvimento onde alterações no código são integradas regularmente em um repositório central, permitindo a automação de testes e validação contínua" (Eric Malvare  Ning Chen, 2023, https://doi.org/10.1109/CSCE60160.2023.00412).  

3. **Conceito terciário:** _Revisão de Código._  
   - Definição: "Processo de inspeção do código por pares com o objetivo de identificar e corrigir defeitos, melhorar a qualidade do software e promover o compartilhamento de conhecimento técnico entre os desenvolvedores" (Hong Yi Lin et al., 2024, https://doi.org/10.1145/3643991.3644910).  

---

## Trabalhos Relacionados

1. **Impacto das Metodologias Ágeis na Eficiência do Desenvolvimento de Software**  
   - O estudo de Karhapää et al. (2024) analisa o impacto das **metodologias ágeis** na entrega contínua de software funcional. Os autores exploram como práticas iterativas e incrementais, combinadas com feedback constante e adaptação às mudanças, resultam em maior eficiência no desenvolvimento de software. O artigo destaca que essas metodologias são essenciais para gerenciar projetos complexos em cenários de rápida evolução tecnológica, permitindo entregas frequentes e ajustáveis às demandas dos stakeholders. Disponível em: [DOI: 10.1109/ACCESS.2024.3414614](https://doi.org/10.1109/ACCESS.2024.3414614).

2. **Automação de Qualidade no Desenvolvimento Ágil com Integração Contínua**  
   - Malvar e Chen (2023) exploram como a **integração contínua** pode melhorar a qualidade e a eficiência em projetos de software ágeis. O estudo analisa a prática de integrar alterações no código regularmente em um repositório central, com a automação de testes e validações. Os autores destacam que essa abordagem não apenas reduz o tempo necessário para identificar erros, mas também aumenta a confiança e a colaboração entre os membros da equipe. Esse trabalho reforça a importância da integração contínua como um componente central das metodologias ágeis. Disponível em: [DOI: 10.1109/CSCE60160.2023.00412](https://doi.org/10.1109/CSCE60160.2023.00412).

3. **Automatizando a Revisão de Código com Modelos Baseados em Experiência**  
   - Lin et al. (2024) investigam como práticas automatizadas de **revisão de código** podem ser aprimoradas ao considerar a experiência dos revisores na criação de modelos de aprendizado de máquina. O estudo destaca que revisões feitas por desenvolvedores mais experientes trazem maior profundidade e correção, promovendo melhorias significativas na qualidade do software. Além disso, os autores discutem como a automação nesse processo reduz a carga de trabalho humano, otimizando o ciclo de desenvolvimento ágil. Disponível em: [DOI: 10.1145/3643991.3644910](https://doi.org/10.1145/3643991.3644910).

   Esses trabalhos fornecem uma visão abrangente e complementar sobre as práticas e ferramentas fundamentais no desenvolvimento de software ágil, alinhando-se aos conceitos de **metodologias ágeis**, **integração contínua** e **revisão de código**. Eles fortalecem a fundamentação teórica ao demonstrar sua aplicação prática e relevância em contextos industriais e acadêmicos.
---

## Materiais e Métodos  

1. **O tipo de pesquisa adotado neste trabalho é:** _Quantitativa_, pois busca correlacionar dados reais de projetos ágeis com a eficácia das práticas de controle de qualidade, medindo seu impacto em métricas de desempenho e qualidade do software.  
2. **Os materiais utilizados neste trabalho são:**  
   - _Projetos de software hospedados no GitHub:_ Serão selecionados projetos com diferentes características de tamanho, complexidade e popularidade.  
- _Projetos do GitHub (https://github.com/):_ Repositórios que utilizam metodologias ágeis.  
   - _API do GitHub (https://docs.github.com/en/rest):_ Para coleta de dados como commits, pull requests e integrações contínuas.  

   - _APIs para coleta de dados:_ Serão utilizadas APIs para acessar informações sobre os projetos, como commits, aprovação de code reviews e integrações contínuas.  
   - _Ferramentas de análise estatística:_ Serão usadas ferramentas como R e Python para realizar as análises estatísticas necessárias para validar as hipóteses.  
3. **Os métodos empregados neste trabalho são:**  
   - _Método de amostragem:_ Seleção de projetos de diferentes tamanhos, complexidades e com adoção de diversas práticas de controle de qualidade.  
   - _Método de análise de correlação:_ Será utilizado para medir o impacto das práticas de controle de qualidade nas métricas de desempenho do projeto, como a frequência de commits, tempo médio de aprovação de code reviews e outros fatores.  
4. **As métricas de avaliação são:**  
   - Frequência de commits: A frequência com que os desenvolvedores realizam commits no repositório, indicativo de atividade e colaboração.  
   - Tempo médio para aprovação de code reviews: O tempo necessário para revisar e aprovar mudanças no código, refletindo a eficiência do processo de revisão.  
5. **As etapas de execução do trabalho são:**  
   - _Seleção de projetos no GitHub:_ A seleção será feita com base em critérios como tamanho da equipe, complexidade do software e adoção de práticas de controle de qualidade.  
   - _Coleta de dados via APIs:_ Utilização de APIs para acessar informações sobre os projetos selecionados, incluindo histórico de commits, aprovações de code reviews e integrações contínuas.  
   - _Análise estatística utilizando métricas definidas:_ Serão realizadas análises estatísticas para correlacionar as práticas de controle de qualidade com as métricas de desempenho do projeto.  
   - _Redação e apresentação dos resultados:_ Os resultados serão analisados, interpretados e apresentados em formato de relatório final.
