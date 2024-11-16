import { create } from "zustand";
import { devtools } from "zustand/middleware"; // Use Zustand's built-in devtools

const useAuthStore = create(
  devtools(
    (set, get) => ({
      allUserData: null,
      loading: false,

      user: () => ({
        user_id: get().allUserData?.user_id || null,
        username: get().allUserData?.username || null,
      }),

      setUser: (user) =>
        set({
          allUserData: user,
        }),

      setLoading: (loading) => set({ loading }),
      isLoggedIn: () => get().allUserData !== null,
    }),
    { name: "AuthStore" } // Optional: provide a name for the store
  )
);

if (import.meta.env.DEV) {
  devtools(useAuthStore); // Use Zustand's built-in devtools in development environment
}

export { useAuthStore };
