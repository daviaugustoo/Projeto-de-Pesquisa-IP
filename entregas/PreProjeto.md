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

1. **O conceito/teoria principal associado a este trabalho é:** _Metodologias Ágeis._ A sua definição neste trabalho é conforme descrita por _P. Karhapää et al. (2024)_, que definem metodologias ágeis como um conjunto de práticas iterativas e incrementais que focam na colaboração constante entre os membros da equipe e o cliente, buscando a entrega contínua de valor.  
   
   > “Metodologias ágeis são abordagens que envolvem ciclos rápidos de desenvolvimento, com feedback constante e adaptações contínuas, priorizando a entrega de software funcional em pequenos incrementos.” (Karhapää et al., 2024).  
   
2. **O conceito/teoria secundário associado a este trabalho é:** _Integração Contínua._ A definição adotada neste trabalho segue a descrição de _Rahman e Roy (2017)_, que abordam a integração contínua como uma prática de desenvolvimento onde os desenvolvedores frequentemente fazem commit de suas alterações em um repositório compartilhado, permitindo a automação da verificação do código por meio de testes.  

   > “A Integração Contínua é uma prática de desenvolvimento onde mudanças no código são integradas de forma regular e frequentemente, permitindo a automação da construção e verificação do software.” (Rahman & Roy, 2017).  

3. **O conceito/teoria terciário associado a este trabalho é:** _Code Review._ A definição de code review neste trabalho segue o conceito de _Beck et al. (2022)_, que discutem os desafios e benefícios da prática, ressaltando sua importância para a qualidade do código e para a disseminação de conhecimento entre os membros da equipe.  

   > “Code review é o processo de revisão do código-fonte realizado por outros membros da equipe para identificar problemas, melhorar a qualidade do código e compartilhar conhecimentos entre os desenvolvedores.” (Beck et al., 2022).

---

## Trabalhos Relacionados  

1. **O trabalho mais relacionado é:** _Karhapää et al. (2024)._ Publicado no ano 2024, é relevante por discutir um processo baseado em evidências para melhorar a qualidade do desenvolvimento ágil, com foco em práticas robustas de controle de qualidade, como a integração contínua e a entrega de software funcional.  
2. **O segundo trabalho mais relacionado é:** _Beck et al. (2022)._ Publicado no ano 2022, é importante por explorar desafios e soluções para integrar requisitos de qualidade em metodologias ágeis, com ênfase no code review como uma técnica chave para melhorar o controle de qualidade.  
3. **O terceiro trabalho mais relacionado é:** _Smith e Jones (2023)._ Publicado no ano 2023, sua relevância está na análise do impacto de diferentes tamanhos de equipe na eficácia das práticas de controle de qualidade, oferecendo insights sobre como características do projeto podem influenciar as técnicas adotadas.

---

## Materiais e Métodos  

1. **O tipo de pesquisa adotado neste trabalho é:** _Quantitativa_, pois busca correlacionar dados reais de projetos ágeis com a eficácia das práticas de controle de qualidade, medindo seu impacto em métricas de desempenho e qualidade do software.  
2. **Os materiais utilizados neste trabalho são:**  
   - _Projetos de software hospedados no GitHub:_ Serão selecionados projetos com diferentes características de tamanho, complexidade e popularidade.  
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
