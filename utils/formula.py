import numpy as np

def get_norm_vector(vector):
    if len(vector.shape) == 1:
        return vector / np.linalg.norm(vector)
    else:
        return vector / np.linalg.norm(vector, axis=1)[:, np.newaxis]

# dot_product(A, B) = Σ(i=1 to n) (A_i * B_i)
def dot_product(vectors, query_vector):
    vectors_array = np.array(vectors)
    query_vector_array = np.array(query_vector)
    similarities = np.dot(vectors_array, query_vector_array)
    return similarities

# cosine_similarity(A, B) = (A • B) / (||A|| * ||B||)
def cosine_similarity(vectors, query_vector):
    norm_vectors = get_norm_vector(vectors)
    norm_query_vector = get_norm_vector(query_vector)
    similarities = np.dot(norm_vectors, norm_query_vector.T)
    return similarities

# euclidean_distance(A, B) = ||A - B||
def euclidean_distance(vectors, query_vector, get_similarity_score=False):
    similarities = np.linalg.norm(vectors - query_vector, axis=1)
    # if get_similarity_score:
    #     similarities = 1 / (1 + similarities)
    return similarities

def hyper_svm_ranking_algorithm_sort(vectors, query_vector, top_k=5, metric=dot_product):
    similarities = metric(vectors, query_vector)
    top_indices = np.argsort(similarities, axis=0)[-top_k:][::-1]
    return top_indices.flatten(), similarities[top_indices].flatten()