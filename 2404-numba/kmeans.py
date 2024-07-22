import numba as nb
import numpy as np


@nb.njit
def distance(p, q):
    return (np.sum((q - p) ** 2)) ** 0.5


@nb.njit
def softmax(x):
    e = np.exp(x / np.linalg.norm(x))
    return e / np.sum(e)


@nb.njit
def closest_centroid(data, centroids, k, i):
    min_dist = np.inf

    for c in range(k):
        d = distance(centroids[c], data[i])
        if d < min_dist:
            closest = c
            min_dist = d

    return closest, min_dist


@nb.jit
def kmeanspp(data, k):
    n_samples = data.shape[0]
    samples_range = np.arange(n_samples)

    # Initialise centroids.
    centroids = np.empty((k, 2))
    centroids[0, :] = data[np.random.randint(n_samples), :]
    centroid_dists = np.empty(n_samples)

    for c in range(1, k):
        for i in range(n_samples):
            _, min_dist = closest_centroid(data, centroids, c, i)
            centroid_dists[i] = min_dist

        centroids[c] = data[np.random.choice(samples_range, p=softmax(centroid_dists))]

    # Create initial clusters.
    clusters = np.empty((n_samples, 2))
    new_centroids = np.empty(centroids.shape)

    # Create objective function measure.
    agg_distances = []

    # Perform clustering.
    while True:
        total_distance = 0

        # Iterate over samples and determine closest centroid and
        # distance from them.
        for i in range(n_samples):
            closest, min_dist = closest_centroid(data, centroids, k, i)
            clusters[i][0] = closest
            clusters[i][1] = min_dist
            total_distance += min_dist

        # Update objective function.
        agg_distances.append(total_distance)

        # Adjust centroids to means of clusters.
        for i in range(k):
            # A cluster can be empty -- if so, just leave the respective
            # centroid where it is.
            if (cluster := data[clusters[:, 0] == i]).size > 0:
                new_centroids[i] = np.mean(cluster, axis=0)

        # Check if converged.
        if np.allclose(centroids, new_centroids):
            break

        # If not, update centroids and repeat.
        centroids = new_centroids.copy()

    return new_centroids, clusters, np.array(agg_distances)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    df = pd.read_csv("g2-2-100.csv")
    data = df.to_numpy()
    data = data[~np.isnan(data).any(axis=1), :]

    max_k = 3

    for k in range(2, max_k + 1):
        centroids, clusters, agg_distances = kmeanspp(data, k)

    fig = plt.figure(figsize=(18, 6))
    ax1 = fig.add_subplot(1, 2, 1)
    for i in range(max_k):
        cluster = data[clusters[:, 0] == i]
        sns.scatterplot(x=cluster[:, 0], y=cluster[:, 1])
    sns.scatterplot(x=centroids[:, 0], y=centroids[:, 1], s=100)

    ax2 = fig.add_subplot(1, 2, 2)
    sns.lineplot(x=range(agg_distances.shape[0]), y=agg_distances)

    fig.savefig("kmeans.png")
