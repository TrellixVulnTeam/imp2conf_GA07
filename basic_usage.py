
from surprise import SVD
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split

# Load the movielens-100k dataset (download it if needed),
data = Dataset.load_builtin('ml-20m')

# sample random trainset and testset
# test set is made of 25% of the ratings.
trainset, testset = train_test_split(data,test_size=.25, random_state=100)

# We'll use the famous SVD algorithm.
algo = SVD(random_state=100)

# Train the algorithm on the trainset, and predict ratings for the testset
algo.fit(trainset)
predictions = algo.test(testset)

# Then compute RMSE
accuracy.rmse(predictions)
