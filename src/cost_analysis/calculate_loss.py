def cost_analysis(fn, fp):
    cost_fn = 4371 * fn
    cost_fp = 280 * fp
    total_cost = cost_fn + cost_fp
    
    print(f"Total Cost of False Negatives: ${cost_fn}\nTotal Cost of False Positives: ${cost_fp}\nTotal Cost Loss: ${total_cost}")