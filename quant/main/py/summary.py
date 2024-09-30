import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import tensorflow as tf

# 读取文章内容
article = """
‘Pony up’: In strategic shift, UAW says added strikes could come ‘at any time’

UAW President Shawn Fain said the union would not expand its strike against the Big Three automakers on Friday, but that the UAW stood ready to add more workers to the picket lines at any time as its labor action enters a new phase.

“We are prepared at any time to call on more locals to stand up and walk out,” Fain said in a livestream update on negotiations. He later added: “We changed the rules. Now there is only one rule – pony up.”

The announcement marks a tactical shift, Fain said. Previously the UAW had announced strike expansions on Fain’s weekly Friday updates. But now, as part of the union’s strategy to keep the automakers off balance, Fain said strike expansions could come at any day of the week, at any time.


This past Wednesday for the first time it announced an expansion midweek, and without warning, when 8,700 UAW members went on strike suddenly at Ford’s largest factory, the Kentucky Truck Plant in Louisville.

“We’re entering a new phase of this strike, and it demands a new approach,” Fain said. “We’re done waiting until Fridays to escalate our strike.”

Fain said that the companies had started to wait until Fridays to make progress in their bargaining positions, and that the union is changing it strategy in order to speed up progress in negotiations.

United Auto Workers union President Shawn Fain speaking on Facebook Live on Friday, warning that the union is ready to strike additional plants with no warning.
United Auto Workers union President Shawn Fain speaking on Facebook Live on Friday, warning that the union is ready to strike additional plants with no warning.
From UAW International Union
“A negotiation requires both sides making movement. If they’re not ready to move, we’re going to give them a push in a language they understand – dollars and cents,” he said.

This is the first time that the union has gone on strike against GM, Ford and Stellantis at the same time. But rather than shut down any of the companies’ US operations completely, the union has targeted its strike against specific facilities, and then expanded the strike gradually in order to increase pressure at the bargaining table.

The Kentucky Truck Plant is a key money maker for Ford, assembling heavy duty pickup trucks and full-size SUVs and producing $25 billion in annual sales, or about one-sixth of its revenue. It also produced an estimated $150 million in profits a week, according to an estimate from Colin Langan, auto analyst at Wells Fargo.

Ford says it’s at its limit
Ford officials told reporters Thursday that the company has gone as far as it can on the additional money it can offer members.

“We have reached our limit. We’ve actually stretched ourselves to get to this point,” said Kumar Galhotra, president of Ford Blue, which is the unit that sells most of Ford’s gasoline-powered cars to consumers. “We are still working to get this done. We’re open to moving some money around within the deal that might fit the union’s needs better, but in terms of cost of deal, we’re there. We have been very clear, we’re at the limit. Going further will hurt our ability to invest in the business as we need to invest.”

Fain mocked that statement from Ford, saying that while Ford has recovered well since the Great Recession, its workers have seen only modest pay increases, which were outweighed by rising prices.

“I found a pathetic irony in that statement,” he said on Friday. “You know who stretched themselves? The Ford workers who didn’t get a single raise for a decade.”

Fain said the union is in a strong bargaining position and has already achieved a lot in negotiations, but not enough to make up for past concessions by workers.

“We’re at the point in this process where we’re looking for one thing only - a deal,” Fain said. “We’re not giving these companies an extra hour, or an extra day. They know what needs to happen, and they know how to get it done. Taking out Kentucky Truck sent a very clear message not only to Ford, but to GM and Stellantis as well. Don’t you dare slow walk us or low ball us. We will take out whatever plants you force us to.”

More layoffs
While the union didn’t increase the number of plants where it is on strike, the number of UAW members off the job increased at two automakers.

Ford on Friday said it was laying off more workers. “Approximately 550 employees have been asked not to report to work beginning Oct. 16,” the company said in a statement. including the Sharonville Transmission Plant, the Dearborn Stamping Plant, the Dearborn Diversified Manufacturing Plant, the Rawsonville Components Plant, the Sterling Axle Plant and the Chicago Stamping Plant.

“This brings Ford’s total to approximately 2,480 employees impacted by strike-related layoffs,” the company added.

Stellantis, which makes cars under the Jeep, Ram, Dodge and Chrysler brands, announced an additional 700 layoffs at two plants, one a transmission plant and one a casting plant, in Kokomo, Indiana. Those plants supply the Toledo Assembly complex that has been on strike since September 15.

The latest layoffs bring Stellantis strike-related layoffs to 1,340. GM has 2,330 on layoff. Ford warned Thursday that there could be 4,600 additional layoffs within the next week at nine other plants due to the lost production at the Kentucky Truck Plant.

The automakers insist they have no choice but to lay off workers who would have nothing to do because of the strikes at other plants. Stellantis said its latest layoffs Friday was because the two Kokomo plants have reached maximum inventory levels of the parts or components they supply for the Jeep Wrangler or Jeep Gladiator built in Toledo.

In most cases the laid-off workers are not eligible to receive unemployment benefits the way they would be if on layoff in other cases.

The union disputes the need for the layoffs, but said the laid-off workers are entitled to the same $500 a week in strike benefits as the nearly 35,000 now on strike.

“That’s them trying to put the squeeze on our members to settle for less,” Fain has previously said about the layoffs. “With their record profits, they don’t have to lay off a single employee.”

Double-digit raises on the table
The companies are on record as offering members an immediate 10% raise to union members and additional raises totaling 10 percentage points or more during the life of the contracts, which are likely to run through the spring of 2028.

The companies are also agreeing to some kind of return of the cost-of-living adjustment (COLA) to union pay scales to protect workers from rising prices. The union gave up the COLA in 2007, as well as traditional pension plans and health care coverage for retirees for workers hired after the concession contracts reached that year.

In addition, a week ago, Fain announced that GM had agreed to a major union demand to place workers at new and planned EV battery plants under the national master agreement at the company.

GM, Ford and Stellatis have all announced plans to shift from traditional gasoline-powered vehicles to electric vehicles, or EVs. That would end the need for the jobs in their current plants that build engines and transmissions.

All three are in the process of building at least three plants each, almost all in joint ventures with Asian battery makers, that will be used to power EVs. All are expected to pay significantly less than UAW members at those engine and transmission plants are now paid.

Going into negotiations, the companies had insisted the battery plant workers would be employees of the joint ventures, not the companies themselves, and that their pay scale would not be included in this contract.

Details of what GM has agreed upon in relation to workers battery plant workers is not yet known, as GM has not confirmed the tentative agreement on the issue. Ford officials have said they also have been negotiating with the union on the battery plant issue and that progress had been made, without giving details.
"""

sentences = nltk.sent_tokenize(article)

# 移除标点符号并转换为小写
def normalize_text(text):
    text = text.lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    return text

# 创建句子向量
def create_sentence_vectors(sentences):
    stop_words = stopwords.words('english')
    sentence_vectors = []
    max_sentence_length = max(len(nltk.word_tokenize(sentence)) for sentence in sentences)
    for sentence in sentences:
        sentence = normalize_text(sentence)
        words = nltk.word_tokenize(sentence)
        vector = [0] * max_sentence_length
        for word in words:
            if word not in stop_words:
                vector[words.index(word)] = 1
        sentence_vectors.append(vector)
    return sentence_vectors

# 计算句子之间的相似度
def similarity_matrix(sentences, sentence_vectors):
    matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                matrix[i][j] = cosine_distance(sentence_vectors[i], sentence_vectors[j])
    return matrix

# 生成文章摘要
def generate_summary(article, num_sentences):
    sentences = nltk.sent_tokenize(article)
    sentence_vectors = create_sentence_vectors(sentences)
    matrix = similarity_matrix(sentences, sentence_vectors)
    
    # Create a TensorFlow graph for PageRank
    scores = tf.constant(1.0 / len(sentences), dtype=tf.float64, shape=(len(sentences), 1))
    damping_factor = 0.85
    
    for _ in range(10):  # You can adjust the number of iterations
        scores = damping_factor * tf.linalg.matmul(matrix, scores) + (1 - damping_factor) / len(sentences)
    
    ranked_scores = scores.numpy()
    ranked_sentences = sorted(((ranked_scores[i][0], sentence) for i, sentence in enumerate(sentences)), reverse=True)
    
    # 检查句子数量是否足够生成摘要
    if num_sentences > len(ranked_sentences):
        num_sentences = len(ranked_sentences)
    
    summary = " ".join([ranked_sentences[i][1] for i in range(num_sentences)])
    return summary

# 输出文章摘要
num_sentences = 30  # 选择要生成的摘要句子数量
summary = generate_summary(article, num_sentences)
print(summary)