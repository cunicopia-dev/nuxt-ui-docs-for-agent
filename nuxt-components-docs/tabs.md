<!-- source: https://ui.nuxt.com/components/tabs --> # Tabs

[Tabs](https://reka-
ui.com/docs/components/tabs)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Tabs.vue)

A set of tab panels that are displayed one at a time.

## Usage

### Items

Use the `items` prop as an array of objects with the following properties:

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `content?: string`
  * `value?: string | number`
  * `disabled?: boolean`
  * `slot?: string`

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account',
        icon: 'i-lucide-user',
        content: 'This is the account content.'
      },
      {
        label: 'Password',
        icon: 'i-lucide-lock',
        content: 'This is the password content.'
      }
    ])
    </script>
    
    <template>
      <UTabs :items="items" class="w-full" />
    </template>
    

### Content

Set the `content` prop to `false` to turn the Tabs into a toggle-only control
without displaying any content. Defaults to `true`.

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account',
        icon: 'i-lucide-user',
        content: 'This is the account content.'
      },
      {
        label: 'Password',
        icon: 'i-lucide-lock',
        content: 'This is the password content.'
      }
    ])
    </script>
    
    <template>
      <UTabs :content="false" :items="items" class="w-full" />
    </template>
    

### Unmount

Use the `unmount-on-hide` prop to prevent the content from being unmounted
when the Tabs is collapsed. Defaults to `true`.

unmountOnHide

false

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account',
        icon: 'i-lucide-user',
        content: 'This is the account content.'
      },
      {
        label: 'Password',
        icon: 'i-lucide-lock',
        content: 'This is the password content.'
      }
    ])
    </script>
    
    <template>
      <UTabs :unmount-on-hide="false" :items="items" class="w-full" />
    </template>
    

You can inspect the DOM to see each item's content being rendered.

### Color

Use the `color` prop to change the color of the Tabs.

color

neutral

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account'
      },
      {
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UTabs color="neutral" :content="false" :items="items" class="w-full" />
    </template>
    

### Variant

Use the `variant` prop to change the variant of the Tabs.

color

neutral

variant

link

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account'
      },
      {
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UTabs color="neutral" variant="link" :content="false" :items="items" class="w-full" />
    </template>
    

### Size

Use the `size` prop to change the size of the Tabs.

size

md

variant

pill

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account'
      },
      {
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UTabs size="md" variant="pill" :content="false" :items="items" class="w-full" />
    </template>
    

### Orientation

Use the `orientation` prop to change the orientation of the Tabs. Defaults to
`horizontal`.

orientation

vertical

variant

pill

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = ref<TabsItem[]>([
      {
        label: 'Account'
      },
      {
        label: 'Password'
      }
    ])
    </script>
    
    <template>
      <UTabs orientation="vertical" variant="pill" :content="false" :items="items" class="w-full" />
    </template>
    

## Examples

### Control active item

You can control the active item by using the `default-value` prop or the
`v-model` directive with the index of the item.

AccountPassword

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items: TabsItem[] = [
      {
        label: 'Account'
      },
      {
        label: 'Password'
      }
    ]
    
    const active = ref('0')
    
    // Note: This is for demonstration purposes only. Don't do this at home.
    onMounted(() => {
      setInterval(() => {
        active.value = String((Number(active.value) + 1) % items.length)
      }, 2000)
    })
    </script>
    
    <template>
      <UTabs v-model="active" :content="false" :items="items" class="w-full" />
    </template>
    

You can also pass the `value` of one of the items if provided.

### With content slot

Use the `#content` slot to customize the content of each item.

AccountPassword

This is the Account tab.

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items: TabsItem[] = [
      {
        label: 'Account',
        icon: 'i-lucide-user'
      },
      {
        label: 'Password',
        icon: 'i-lucide-lock'
      }
    ]
    </script>
    
    <template>
      <UTabs :items="items" class="w-full">
        <template #content="{ item }">
          <p>This is the {{ item.label }} tab.</p>
        </template>
      </UTabs>
    </template>
    

### With custom slot

Use the `slot` property to customize a specific item.

AccountPassword

Make changes to your account here. Click save when you're done.

Name

Username

Save changes

    
    
    <script setup lang="ts">
    import type { TabsItem } from '@nuxt/ui'
    
    const items = [
      {
        label: 'Account',
        description: 'Make changes to your account here. Click save when you\'re done.',
        icon: 'i-lucide-user',
        slot: 'account' as const
      },
      {
        label: 'Password',
        description: 'Change your password here. After saving, you\'ll be logged out.',
        icon: 'i-lucide-lock',
        slot: 'password' as const
      }
    ] satisfies TabsItem[]
    
    const state = reactive({
      name: 'Benjamin Canac',
      username: 'benjamincanac',
      currentPassword: '',
      newPassword: '',
      confirmPassword: ''
    })
    </script>
    
    <template>
      <UTabs :items="items" variant="link" class="gap-4 w-full" :ui="{ trigger: 'flex-1' }">
        <template #account="{ item }">
          <p class="text-muted mb-4">
            {{ item.description }}
          </p>
    
          <UForm :state="state" class="flex flex-col gap-4">
            <UFormField label="Name" name="name">
              <UInput v-model="state.name" class="w-full" />
            </UFormField>
            <UFormField label="Username" name="username">
              <UInput v-model="state.username" class="w-full" />
            </UFormField>
    
            <UButton label="Save changes" type="submit" variant="soft" class="self-end" />
          </UForm>
        </template>
    
        <template #password="{ item }">
          <p class="text-muted mb-4">
            {{ item.description }}
          </p>
    
          <UForm :state="state" class="flex flex-col gap-4">
            <UFormField label="Current Password" name="current" required>
              <UInput v-model="state.currentPassword" type="password" required class="w-full" />
            </UFormField>
            <UFormField label="New Password" name="new" required>
              <UInput v-model="state.newPassword" type="password" required class="w-full" />
            </UFormField>
            <UFormField label="Confirm Password" name="confirm" required>
              <UInput v-model="state.confirmPassword" type="password" required class="w-full" />
            </UFormField>
    
            <UButton label="Change password" type="submit" variant="soft" class="self-end" />
          </UForm>
        </template>
      </UTabs>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`items`| | ` TabsItem[]`Show properties

  * `label?: string`
  * `icon?: string`
  * `avatar?: AvatarProps`
  * `slot?: string`
  * `content?: string`
  * `value?: string | number`A unique value for the tab item. Defaults to the index.
  * `disabled?: boolean`

  
`color`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`  
`variant`| `'pill'`| ` "pill" | "link"`  
`size`| `'md'`| ` "xs" | "md" | "sm" | "lg" | "xl"`  
`orientation`| `'horizontal'`| ` "horizontal" | "vertical"`The orientation of the tabs.  
`content`| `true`| `boolean`The content of the tabs, can be disabled to
prevent rendering the content.  
`labelKey`| `'label'`| ` string`The key used to get the label from the item.  
`defaultValue`| `'0'`| ` string | number`The value of the tab that should be active when initially rendered. Use when you do not need to control the state of the tabs  
`modelValue`| | ` string | number`The controlled value of the tab to activate. Can be bind as `v-model`.  
`activationMode`| `automatic`| ` "automatic" | "manual"`Whether a tab is activated automatically (on focus) or manually (on click).  
`unmountOnHide`| `true`| `boolean`When `true`, the element will be unmounted
on closed state.  
`ui`| | ` { root?: ClassNameValue; list?: ClassNameValue; indicator?: ClassNameValue; trigger?: ClassNameValue; content?: ClassNameValue; leadingIcon?: ClassNameValue; leadingAvatar?: ClassNameValue; leadingAvatarSize?: ClassNameValue; label?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`leading`| `{ item: TabsItem; index: number; }`  
`default`| `{ item: TabsItem; index: number; }`  
`trailing`| `{ item: TabsItem; index: number; }`  
`content`| `{ item: TabsItem; index: number; }`  
`list-leading`| `{}`  
`list-trailing`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:modelValue`| `[payload: string | number]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        tabs: {
          slots: {
            root: 'flex items-center gap-2',
            list: 'relative flex p-1 group',
            indicator: 'absolute transition-[translate,width] duration-200',
            trigger: [
              'group relative inline-flex items-center shrink-0 min-w-0 data-[state=inactive]:text-muted hover:data-[state=inactive]:not-disabled:text-default font-medium rounded-md disabled:cursor-not-allowed disabled:opacity-75',
              'transition-colors'
            ],
            content: 'focus:outline-none w-full',
            leadingIcon: 'shrink-0',
            leadingAvatar: 'shrink-0',
            leadingAvatarSize: '',
            label: 'truncate'
          },
          variants: {
            color: {
              primary: '',
              secondary: '',
              success: '',
              info: '',
              warning: '',
              error: '',
              neutral: ''
            },
            variant: {
              pill: {
                list: 'bg-elevated rounded-lg',
                trigger: 'flex-1 w-full',
                indicator: 'rounded-md shadow-xs'
              },
              link: {
                list: 'border-default',
                indicator: 'rounded-full'
              }
            },
            orientation: {
              horizontal: {
                root: 'flex-col',
                list: 'w-full',
                indicator: 'left-0 w-(--reka-tabs-indicator-size) translate-x-(--reka-tabs-indicator-position)',
                trigger: 'justify-center'
              },
              vertical: {
                list: 'flex-col',
                indicator: 'top-0 h-(--reka-tabs-indicator-size) translate-y-(--reka-tabs-indicator-position)'
              }
            },
            size: {
              xs: {
                trigger: 'px-2 py-1 text-xs gap-1',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs'
              },
              sm: {
                trigger: 'px-2.5 py-1.5 text-xs gap-1.5',
                leadingIcon: 'size-4',
                leadingAvatarSize: '3xs'
              },
              md: {
                trigger: 'px-3 py-1.5 text-sm gap-1.5',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs'
              },
              lg: {
                trigger: 'px-3 py-2 text-sm gap-2',
                leadingIcon: 'size-5',
                leadingAvatarSize: '2xs'
              },
              xl: {
                trigger: 'px-3 py-2 text-base gap-2',
                leadingIcon: 'size-6',
                leadingAvatarSize: 'xs'
              }
            }
          },
          compoundVariants: [
            {
              orientation: 'horizontal',
              variant: 'pill',
              class: {
                indicator: 'inset-y-1'
              }
            },
            {
              orientation: 'horizontal',
              variant: 'link',
              class: {
                list: 'border-b -mb-px',
                indicator: '-bottom-px h-px'
              }
            },
            {
              orientation: 'vertical',
              variant: 'pill',
              class: {
                indicator: 'inset-x-1',
                list: 'items-center'
              }
            },
            {
              orientation: 'vertical',
              variant: 'link',
              class: {
                list: 'border-s -ms-px',
                indicator: '-start-px w-px'
              }
            },
            {
              color: 'primary',
              variant: 'pill',
              class: {
                indicator: 'bg-primary',
                trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'pill',
              class: {
                indicator: 'bg-inverted',
                trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
              }
            },
            {
              color: 'primary',
              variant: 'link',
              class: {
                indicator: 'bg-primary',
                trigger: 'data-[state=active]:text-primary focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
              }
            },
            {
              color: 'neutral',
              variant: 'link',
              class: {
                indicator: 'bg-inverted',
                trigger: 'data-[state=active]:text-highlighted focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
              }
            }
          ],
          defaultVariants: {
            color: 'primary',
            variant: 'pill',
            size: 'md'
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            tabs: {
              slots: {
                root: 'flex items-center gap-2',
                list: 'relative flex p-1 group',
                indicator: 'absolute transition-[translate,width] duration-200',
                trigger: [
                  'group relative inline-flex items-center shrink-0 min-w-0 data-[state=inactive]:text-muted hover:data-[state=inactive]:not-disabled:text-default font-medium rounded-md disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                content: 'focus:outline-none w-full',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                label: 'truncate'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: {
                    list: 'bg-elevated rounded-lg',
                    trigger: 'flex-1 w-full',
                    indicator: 'rounded-md shadow-xs'
                  },
                  link: {
                    list: 'border-default',
                    indicator: 'rounded-full'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'flex-col',
                    list: 'w-full',
                    indicator: 'left-0 w-(--reka-tabs-indicator-size) translate-x-(--reka-tabs-indicator-position)',
                    trigger: 'justify-center'
                  },
                  vertical: {
                    list: 'flex-col',
                    indicator: 'top-0 h-(--reka-tabs-indicator-size) translate-y-(--reka-tabs-indicator-position)'
                  }
                },
                size: {
                  xs: {
                    trigger: 'px-2 py-1 text-xs gap-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs'
                  },
                  sm: {
                    trigger: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs'
                  },
                  md: {
                    trigger: 'px-3 py-1.5 text-sm gap-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  lg: {
                    trigger: 'px-3 py-2 text-sm gap-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  xl: {
                    trigger: 'px-3 py-2 text-base gap-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  variant: 'pill',
                  class: {
                    indicator: 'inset-y-1'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'link',
                  class: {
                    list: 'border-b -mb-px',
                    indicator: '-bottom-px h-px'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'pill',
                  class: {
                    indicator: 'inset-x-1',
                    list: 'items-center'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'link',
                  class: {
                    list: 'border-s -ms-px',
                    indicator: '-start-px w-px'
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  class: {
                    indicator: 'bg-primary',
                    trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  class: {
                    indicator: 'bg-inverted',
                    trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  class: {
                    indicator: 'bg-primary',
                    trigger: 'data-[state=active]:text-primary focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  class: {
                    indicator: 'bg-inverted',
                    trigger: 'data-[state=active]:text-highlighted focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'pill',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            tabs: {
              slots: {
                root: 'flex items-center gap-2',
                list: 'relative flex p-1 group',
                indicator: 'absolute transition-[translate,width] duration-200',
                trigger: [
                  'group relative inline-flex items-center shrink-0 min-w-0 data-[state=inactive]:text-muted hover:data-[state=inactive]:not-disabled:text-default font-medium rounded-md disabled:cursor-not-allowed disabled:opacity-75',
                  'transition-colors'
                ],
                content: 'focus:outline-none w-full',
                leadingIcon: 'shrink-0',
                leadingAvatar: 'shrink-0',
                leadingAvatarSize: '',
                label: 'truncate'
              },
              variants: {
                color: {
                  primary: '',
                  secondary: '',
                  success: '',
                  info: '',
                  warning: '',
                  error: '',
                  neutral: ''
                },
                variant: {
                  pill: {
                    list: 'bg-elevated rounded-lg',
                    trigger: 'flex-1 w-full',
                    indicator: 'rounded-md shadow-xs'
                  },
                  link: {
                    list: 'border-default',
                    indicator: 'rounded-full'
                  }
                },
                orientation: {
                  horizontal: {
                    root: 'flex-col',
                    list: 'w-full',
                    indicator: 'left-0 w-(--reka-tabs-indicator-size) translate-x-(--reka-tabs-indicator-position)',
                    trigger: 'justify-center'
                  },
                  vertical: {
                    list: 'flex-col',
                    indicator: 'top-0 h-(--reka-tabs-indicator-size) translate-y-(--reka-tabs-indicator-position)'
                  }
                },
                size: {
                  xs: {
                    trigger: 'px-2 py-1 text-xs gap-1',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs'
                  },
                  sm: {
                    trigger: 'px-2.5 py-1.5 text-xs gap-1.5',
                    leadingIcon: 'size-4',
                    leadingAvatarSize: '3xs'
                  },
                  md: {
                    trigger: 'px-3 py-1.5 text-sm gap-1.5',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  lg: {
                    trigger: 'px-3 py-2 text-sm gap-2',
                    leadingIcon: 'size-5',
                    leadingAvatarSize: '2xs'
                  },
                  xl: {
                    trigger: 'px-3 py-2 text-base gap-2',
                    leadingIcon: 'size-6',
                    leadingAvatarSize: 'xs'
                  }
                }
              },
              compoundVariants: [
                {
                  orientation: 'horizontal',
                  variant: 'pill',
                  class: {
                    indicator: 'inset-y-1'
                  }
                },
                {
                  orientation: 'horizontal',
                  variant: 'link',
                  class: {
                    list: 'border-b -mb-px',
                    indicator: '-bottom-px h-px'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'pill',
                  class: {
                    indicator: 'inset-x-1',
                    list: 'items-center'
                  }
                },
                {
                  orientation: 'vertical',
                  variant: 'link',
                  class: {
                    list: 'border-s -ms-px',
                    indicator: '-start-px w-px'
                  }
                },
                {
                  color: 'primary',
                  variant: 'pill',
                  class: {
                    indicator: 'bg-primary',
                    trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'pill',
                  class: {
                    indicator: 'bg-inverted',
                    trigger: 'data-[state=active]:text-inverted focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-inverted'
                  }
                },
                {
                  color: 'primary',
                  variant: 'link',
                  class: {
                    indicator: 'bg-primary',
                    trigger: 'data-[state=active]:text-primary focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-primary'
                  }
                },
                {
                  color: 'neutral',
                  variant: 'link',
                  class: {
                    indicator: 'bg-inverted',
                    trigger: 'data-[state=active]:text-highlighted focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-inverted'
                  }
                }
              ],
              defaultVariants: {
                color: 'primary',
                variant: 'pill',
                size: 'md'
              }
            }
          }
        })
      ]
    })
    

Expand code

[](https://github.com/nuxt/ui/blob/v3/src/theme/tabs.ts "Compound
variants")Some colors in `compoundVariants` are omitted for readability. Check
out the source code on GitHub.

[TableA responsive table element to display data in rows and
columns.](/components/table)[TextareaA textarea element to input multi-line
text.](/components/textarea)

