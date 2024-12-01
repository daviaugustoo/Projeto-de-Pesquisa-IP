# Avaliação de Técnicas de Controle de Qualidade no Desenvolvimento de Software Utilizando Metodologias Ágeis

## Equipe

1. Davi Augusto Dias Soares  
2. Victor Lucas Tornelli  

* **Orientador de Conteúdo:** Lesandro Ponciano

## Resumo
A integração de metodologias ágeis nos processos de desenvolvimento de software destacou a necessidade de práticas robustas de controle de qualidade. Este trabalho busca avaliar o impacto de técnicas de desenvolvimento, como  revisão de código e integração contínua, na eficiência e eficácia do desenvolvimento de software ágil. Para tanto, utiliza-se um conjunto diversificado de repositórios de software hospedados no GitHub e analisa-se métricas como densidade de defeitos e produtividade das equipes. O estudo propõe uma abordagem quantitativa baseada na análise estatística para correlacionar as técnicas adotadas com o desempenho dos projetos.

---

## **Introdução**  

   Este trabalho investiga a **avaliação de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis.** O crescente uso de metodologias ágeis no desenvolvimento de software trouxe desafios relacionados à garantia da qualidade dos produtos entregues. Em ambientes ágeis, como as diferentes técnicas de controle de qualidade impactam a eficiência e a eficácia do ciclo de desenvolvimento?  
   
   As metodologias ágeis, caracterizadas por ciclos curtos de desenvolvimento, colaboração constante e entregas incrementais, se tornaram predominantes na indústria de software. No entanto, a velocidade e a flexibilidade promovidas por essas metodologias podem, em alguns casos, comprometer práticas robustas de controle de qualidade se não forem implementadas adequadamente. De acordo com Karhapää et al. (2024), falhas nas técnicas de controle de qualidade são responsáveis por atrasos, aumento de custos e redução na confiabilidade do software. Identificar e analisar os impactos de técnicas como testes automatizados, revisões de código e integração contínua é essencial para assegurar que os princípios ágeis sejam mantidos sem comprometer a qualidade.  

   Além disso, a adoção de práticas de controle de qualidade não é uniforme entre as equipes de desenvolvimento. Características como tamanho da equipe, complexidade do projeto e recursos disponíveis influenciam diretamente a escolha e a eficácia dessas técnicas. A compreensão dessas variáveis pode orientar melhores práticas, promovendo entregas mais confiáveis e consistentes.  

  O objetivo geral é valiar o impacto de técnicas de controle de qualidade no desenvolvimento de software utilizando metodologias ágeis, analisando sua eficácia em manter a qualidade e a eficiência dos projetos. Este pode ser dividido em objetivos específicos:
   - Comparar as técnicas de controle de qualidade mais utilizadas, como testes automatizados, revisão de código e integração contínua, no contexto de projetos ágeis.  
   - Avaliar o impacto dessas técnicas em métricas específicas do desenvolvimento, como densidade de defeitos, produtividade das equipes e frequência de refatorações.  
   - Identificar como características dos projetos, como tamanho da equipe, popularidade e complexidade, influenciam a adoção e eficácia das técnicas de controle de qualidade.  

   Este documento apresenta os conceitos-chave e práticas abordadas, discute estudos anteriores que embasam este trabalho, descreve a abordagem adotada para coleta e análise de dados e, finalmente aborda as contribuições esperadas e implicações práticas do estudo.  

### **Contribuições do estudo**  
Espera-se que os resultados deste trabalho forneçam uma visão prática e baseada em evidências sobre a eficácia de diferentes técnicas de controle de qualidade em ambientes ágeis. Além de orientar equipes de desenvolvimento na seleção de práticas adequadas, os resultados poderão contribuir para a elaboração de diretrizes mais robustas para a integração da qualidade no contexto ágil.  

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
